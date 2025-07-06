import itertools
import math
import random
import numpy as np

from utils import is_satisfied, kendall_tau_distance, squared_kendall_tau_distance


def run_tspf(profile_sequence, spf, update_function, initialization, threshold):
    """Runs the temporal social preference function with the given parameters.

    :param profile_sequence: List of preference profiles that represent different rounds. 
    :param spf: Social preference function.
    :param update_function: Weight update function.
    :param initialization: Weight initialization as a list of non-negative integers.
    :param threshold: Satisfaction threshold.
    
    :return: Tuple of output rankings, satisfaction and support of each voter in each round.
    """
    weights = initialize_weights(profile_sequence, initialization)
    
    results = [] # List of output rankings
    for current_time_step_profile in profile_sequence:
        result = run_spf(current_time_step_profile, weights, spf)
        weights = update_weights(weights, current_time_step_profile, update_function, result, threshold)
        results.append(result)
    satisfaction_matrix = compute_satisfaction(profile_sequence, results, threshold)
    support_matrix = compute_support(profile_sequence, threshold)
    return results, satisfaction_matrix, support_matrix

def initialize_weights(profile_sequence, initialization="equal"):
    """Initializes the weights before the first round.

    :param profile_sequence: List of preference profiles that represent different rounds.
    :param initialization: Initialization strategy, "equal", where every voter has the weight 1, 
    or "special-voter-25-percent", where every voter except the special one has 1, special voter
    at least 25% of the total weight.

    :return: Array of weights.
    """
    num_voters_round_one = len(profile_sequence[0])
    if initialization == "equal":
        return np.ones(num_voters_round_one)
    elif initialization == "special-voter-25-percent":
        three_quarter_total_weight = len(profile_sequence[0]) - 1
        weights = np.ones(num_voters_round_one)
        weights[len(profile_sequence[0]) - 1] = math.ceil(three_quarter_total_weight / 3)
        return weights

def run_spf(profile, weights, spf):
    """Runs the specified social preference function.

    :param profile: Preference profile.
    :param weights: Array of weights.
    :param spf: Social preference function. "borda" for weighted Borda, 
    "kemeny" for weighted Kemeny, "sq-kemeny" for squared Kemeny, 
    "rsd" for random serial dictatorship, "weighted-rsd" for weighted random serial dictatorship.

    :return: Output ranking.
    """
    if spf == "borda":
        return run_weighted_borda(profile, weights)
    elif spf == "kemeny":
        return run_weighted_kemeny(profile, weights)
    elif spf == "sq-kemeny":
        return run_weighted_kemeny(profile, weights, True)
    elif spf == "rsd":
        return run_random_serial_dictatorship(profile)
    elif spf == "weighted-rsd":
        return run_weighted_random_serial_dictatorship(profile, weights)
    else:
        raise NotImplementedError("Social preference function " + spf + " is unknown.")

def update_weights(weights, profile, update_function, output_ranking, threshold=0):
    """Updates the weights.
    
    :param weights: Array of weights.
    :param profile: Preference profile.
    :param update_function: Specified weight update function
    :param output_ranking: Output ranking.
    :param threshold: Satisfaction threshold.

    :return Array of weights.
    """
    if update_function == "constant":
        return weights
    elif update_function == "myopic-kt":
        return update_myopic_kt(weights, profile, output_ranking)
    elif update_function == "myopic-sq-kt":
        return update_myopic_sq_kt(weights, profile, output_ranking)
    elif update_function == "kt":
        return update_kt(weights, profile, output_ranking)
    elif update_function == "sq-kt":
        return update_sq_kt(weights, profile, output_ranking)
    elif update_function == "unit-cost":
        return update_unit_cost(weights, profile, threshold, output_ranking)
    elif update_function == "kt-reset":
        return update_kt_reset(weights, profile, threshold, output_ranking)
    elif update_function == "unit-cost-reset":
        return update_unit_cost_reset(weights, profile, threshold, output_ranking)
    elif update_function == "special-voter-kt":
        pass
    elif update_function == "perpetual-kt":
        return update_perpetual_kt(weights, profile, threshold, output_ranking)
    elif update_function == "perpetual-nash":
        pass
    elif update_function:
        raise NotImplementedError("Weight update function " + str(update_function) + " is unknown.")
    return weights

def run_weighted_borda(profile, weights):
    num_candidates = len(profile[0])
    
    # Initialize Borda scores
    scores = np.zeros(num_candidates, dtype=int)

    # For each voter, assign Borda scores (m-1 to 0)
    for voter_index, ranking in enumerate(profile):
        weight = weights[voter_index]
        for i, candidate in enumerate(ranking):
            scores[candidate] += weight * (num_candidates - 1 - i)

    # Tiebreaker: use the last voter's ranking
    tiebreaker = {candidate: rank for rank, candidate in enumerate(profile[len(profile)-1])}

    # Sort candidates by descending score, then by tiebreaker (ascending ranks)
    output_ranking = sorted(range(num_candidates), key=lambda c: (scores[c], -tiebreaker[c]), reverse=True)

    return output_ranking

def run_weighted_kemeny(profile, weights, squared_kemeny=False):
    num_candidates = len(profile[0])
    candidates = list(range(num_candidates))
    
    min_total_distance = float('inf')
    best_ranking = None

    for guess_ranking in itertools.permutations(candidates):
        if squared_kemeny:
            total_distance = sum((weights[voter_index] * squared_kendall_tau_distance(guess_ranking, voter_ranking)) for voter_index, voter_ranking in enumerate(profile))
        else:
            total_distance = sum((weights[voter_index] * kendall_tau_distance(guess_ranking, voter_ranking)) for voter_index, voter_ranking in enumerate(profile))

        if total_distance == min_total_distance:
            num_voters = len(profile)
            special_voter = profile[num_voters-1]
            if squared_kemeny:
                if squared_kendall_tau_distance(special_voter, guess_ranking) <= squared_kendall_tau_distance(special_voter, best_ranking):
                    total_distance = min_total_distance
                    best_ranking = guess_ranking
            else:
                if kendall_tau_distance(special_voter, guess_ranking) <= kendall_tau_distance(special_voter, best_ranking):
                    total_distance = min_total_distance
                    best_ranking = guess_ranking
        if total_distance < min_total_distance:
            min_total_distance = total_distance
            best_ranking = guess_ranking

    return list(best_ranking)    

def run_random_serial_dictatorship(profile):
    return random.choice(profile)

def run_weighted_random_serial_dictatorship(profile, weights):
    return random.choices(profile, weights=weights, k=1)[0]


def update_unit_cost(weights, profile, threshold, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        if not is_satisfied(voter_ranking, output_ranking, threshold):
            weights[voter_index] += 1
    return weights

def update_kt_reset(weights, profile, threshold, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        if not is_satisfied(voter_ranking, output_ranking, threshold):
            weights[voter_index] += kendall_tau_distance(voter_ranking, output_ranking)
        else:
            weights[voter_index] = 1
    return weights

def update_unit_cost_reset(weights, profile, threshold, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        if not is_satisfied(voter_ranking, output_ranking, threshold):
            weights[voter_index] += 1
        else:
            weights[voter_index] = 1
    return weights

def update_myopic_kt(weights, profile, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        weights[voter_index] = kendall_tau_distance(voter_ranking, output_ranking)
    return weights

def update_myopic_sq_kt(weights, profile, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        weights[voter_index] = squared_kendall_tau_distance(voter_ranking, output_ranking)
    return weights

def update_kt(weights, profile, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        weights[voter_index] += kendall_tau_distance(voter_ranking, output_ranking)
    return weights

def update_sq_kt(weights, profile, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        weights[voter_index] += squared_kendall_tau_distance(voter_ranking, output_ranking)
    return weights

def update_perpetual_kt(weights, profile, threshold, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        if is_satisfied(voter_ranking, output_ranking, threshold):
            weights[voter_index] = weights[voter_index] / (weights[voter_index] + 1)
    return weights

def compute_satisfaction(profile_sequence, results, threshold):
    num_rounds = len(profile_sequence)
    num_voters = len(profile_sequence[0])
    
    satisfaction_matrix = []
    for i in range(num_rounds):
        row = []
        for j in range(num_voters):
            row.append(0)
        satisfaction_matrix.append(row)

    for i, profile in enumerate(profile_sequence):
        for j, voter in enumerate(profile):
            if is_satisfied(voter, results[i], threshold):
                satisfaction_matrix[i][j] = 1
    return satisfaction_matrix

def compute_support(profile_sequence, threshold):
    num_rounds = len(profile_sequence)
    num_voters = len(profile_sequence[0])
    
    support_matrix = []
    for i in range(num_rounds):
        row = []
        for j in range(num_voters):
            row.append(0)
        support_matrix.append(row)

    for i, profile in enumerate(profile_sequence):
        for j, voter in enumerate(profile):
            for other_voters in profile:
                if is_satisfied(voter, other_voters, threshold):
                    support_matrix[i][j] += 1
    return support_matrix