import itertools
import random
import numpy as np


def run_dspf(profile_sequence, spf, update_function, initialization):
    weights = initialize_weights(profile_sequence)
    print(profile_sequence)
    results = [] # List of tuples of (round, output_ranking), maybe also statistics as a third element of tuple
    for t, current_time_step_profile in enumerate(profile_sequence, 1):
        result = run_spf(current_time_step_profile, weights, spf)
        weights = update_weights(weights, current_time_step_profile, update_function, result)
        results.append((t, result))
    return results

def initialize_weights(profile_sequence):
    num_voters_round_one = len(profile_sequence[0])
    return np.ones(num_voters_round_one) 

def run_spf(profile, weights, spf):
    if spf == "borda":
        return run_weighted_borda(profile, weights)
    elif spf == "kemeny":
        return run_weighted_kemeny(profile, weights)
    elif spf == "sq-kemeny":
        return run_weighted_kemeny(profile, weights, True)
    elif spf == "rsd":
        return run_random_dictatorship(profile)
    else:
        raise NotImplementedError("Social preference function " + spf + " is unknown.")

def update_weights(weights, profile, update_function, output_ranking, threshold=0):
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
        pass
    elif update_function == "perpetual-nash":
        pass
    else:
        raise NotImplementedError("Weight update function " + update_function + " is unknown.")
    return weights

def run_weighted_borda(profile, weights):
    num_candidates = len(profile[0])
    
    # Initialize Borda scores
    scores = np.ones(num_candidates, dtype=int)
    
    # For each voter, assign Borda scores (m-1 to 0)
    for voter_index, ranking in enumerate(profile):
        weight = weights[voter_index]
        for i, candidate in enumerate(ranking):
            scores[candidate] += weight * (num_candidates - 1 - i)
    
    # Create output ranking: sort candidates by descending score
    output_ranking = list(np.argsort(-scores))
    print(scores)
    print(output_ranking)
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
        if total_distance < min_total_distance:
        #    print("NOT THIS ONE")
        #    print(total_distance)
            min_total_distance = total_distance
            best_ranking = guess_ranking
    print(min_total_distance)
    print(best_ranking)
    return list(best_ranking)    

def run_random_dictatorship(profile):
    # rotational serial dictatorship could be tried as well, voters that have already won get the weight 0 until all voters become 0, then reset everything to 1
    return random.choice(profile)

def kendall_tau_distance(r1, r2):
    """Compute the Kendall tau distance between two rankings.
    
    :param r1: Preference ranking 1
    :param r2: Preference ranking 2
    """
    index_r1 = {c: i for i, c in enumerate(r1)}
    index_r2 = {c: i for i, c in enumerate(r2)}
    print(index_r1, index_r2)
    distance = 0
    n = len(r1)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = r1[i], r1[j]
 #           print(a, b)
  #          print("HERE")
   #         print(index_r1[a], index_r1[b])
    #        print(index_r2[a], index_r2[b])
            if (index_r1[a] < index_r1[b] and index_r2[a] > index_r2[b]):
                #print("There")
                distance += 1
   # print(str(r1) + " and " + str(r2))
    #print("KT: ", distance)
    return distance

def squared_kendall_tau_distance(r1, r2):
    """Compute the squared Kendall tau distance between two rankings.
    
    :param r1: Preference ranking 1
    :param r2: Preference ranking 2
    """
    return kendall_tau_distance(r1, r2) ** 2

def is_satisfied(threshold, voter_ranking, output_ranking):
    if kendall_tau_distance(voter_ranking, output_ranking) <= threshold:
        return True
    return False

def update_unit_cost(weights, profile, threshold, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        if not is_satisfied(threshold, voter_ranking, output_ranking):
            weights[voter_index] += 1
    return weights

def update_kt_reset(weights, profile, threshold, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        if not is_satisfied(threshold, voter_ranking, output_ranking):
            weights[voter_index] += kendall_tau_distance(voter_ranking, output_ranking)
        else:
            weights[voter_index] = 1
    return weights

def update_unit_cost_reset(weights, profile, threshold, output_ranking):
    for voter_index, voter_ranking in enumerate(profile):
        if not is_satisfied(threshold, voter_ranking, output_ranking):
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