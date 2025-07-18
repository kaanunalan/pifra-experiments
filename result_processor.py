import math
import numpy as np

from utils import kendall_tau_distance, spearman_footrule_distance, squared_kendall_tau_distance


def analyze_results(profile_sequence, results, satisfaction_matrix, support_matrix):
    pass
    #print("Perpetual Lower Quota Compliance:")
    #print(get_perpetual_lower_quota_compliance(satisfaction_matrix, support_matrix))
    #print()
    #print("Gini Influence Coefficient:")
    #print(get_gini_influence_coefficient(profile_sequence, results, satisfaction_matrix))
    #print()
    #print("Average Spearman Footrule Distance:")
    #print(get_avg_spearman_footrule_distance(profile_sequence, results))
    #print()
    #print("Average KT Distance:")
    #print(get_avg_kt_distance(profile_sequence, results))
    #print()
    #print("Standard Deviation of KT Distance:")
    #print(get_standard_deviation_kt(profile_sequence, results))
    #print()
    #print("Get Egalitarian KT Distance:")
    #print(get_egalitarian_kt_distance(profile_sequence, results))
    #print()

def get_perpetual_lower_quota_compliance(satisfaction_matrix, support_matrix):
    num_voters = len(satisfaction_matrix[0])
    num_rounds = len(satisfaction_matrix)
    
    compl_counter = 0
    for t in range(num_rounds):
        for v in range(num_voters):
            sat = sum(satisfaction_matrix[round_ind][v] for round_ind in range(t))
            quota = sum(support_matrix[round_ind][v] for round_ind in range(t))

            if sat >= math.floor(quota):
                compl_counter += 1

    return compl_counter / (num_voters * num_rounds)

def get_perpetual_lower_quota_compliance_ratio_special_voter(satisfaction_matrix, support_matrix):
    num_voters = len(satisfaction_matrix[0])
    num_rounds = len(satisfaction_matrix)
    
    compl_counter = 0
    compl_counter_special_voter = 0
    for t in range(num_rounds):
        for v in range(num_voters-1): # Do not include the special voter
            sat = sum(satisfaction_matrix[round_ind][v] for round_ind in range(t))
            quota = sum(support_matrix[round_ind][v] for round_ind in range(t))

            if sat >= math.floor(quota):
                compl_counter += 1
        
        sat_special_voter = sum(satisfaction_matrix[round_ind][num_voters - 1] for round_ind in range(num_rounds))
        quota_special_voter = sum(support_matrix[round_ind][num_voters - 1] for round_ind in range(num_rounds))
        if sat_special_voter >= math.floor(quota_special_voter):
            compl_counter_special_voter += 1

    perpetual_lower_quota_excluding_special_voter = compl_counter / ((num_voters - 1) * num_rounds)
    perpetual_lower_quota_special_voter = compl_counter_special_voter / num_rounds
   
    return perpetual_lower_quota_special_voter / perpetual_lower_quota_excluding_special_voter if perpetual_lower_quota_excluding_special_voter != 0 else -1

def get_gini_influence_coefficient(profile_sequence, result_sequence, sat_matrix):
    num_voters = len(profile_sequence[0])
    a = get_avg_infl(profile_sequence, result_sequence, sat_matrix)
    sum_infl_diff = 0
    for u in range(num_voters):
        infl_u = get_voter_influence(profile_sequence, result_sequence, u, sat_matrix)
        for v in range(num_voters):
            infl_v = get_voter_influence(profile_sequence, result_sequence, v, sat_matrix)
            sum_infl_diff += abs(infl_u - infl_v)
    if a != 0:
        return sum_infl_diff / (2 * a * num_voters * num_voters)
    else:
        return 0
    
def get_voter_influence(profile_sequence, result_sequence,  voter_index, sat_matrix):
    num_rounds = len(result_sequence)
    
    infl_counter = 0
    sat_counter_v = 0
    sat_counter_u = 0
    for t in range(num_rounds):
        if sat_matrix[t][voter_index] == 1:
            sat_counter_v += 1
        for u_ind, _ in enumerate(profile_sequence[t]):
            if sat_matrix[t][u_ind] == 1:
                sat_counter_u += 1
        if sat_counter_u != 0:
            infl_counter += sat_counter_v / sat_counter_u
    return infl_counter

def get_avg_infl(profile_sequence, result_sequence, sat_matrix):
    num_voters = len(profile_sequence[0])
    sum_infl = 0
    for v_ind in range(num_voters):
        sum_infl += get_voter_influence(profile_sequence, result_sequence, v_ind, sat_matrix)
    return sum_infl / num_voters

def get_avg_spearman_footrule_distance(profile_sequence, result_sequence):
    num_voters = len(profile_sequence[0])
    total_distance = 0.0

    for t in range(len(result_sequence)):
        output = result_sequence[t]
        profile = profile_sequence[t]
        avg_distance_this_round = sum(spearman_footrule_distance(output, voter) for voter in profile) / num_voters
        total_distance += avg_distance_this_round
    return total_distance / len(result_sequence)

def get_avg_kt_distance(profile_sequence, result_sequence):
    num_voters = len(profile_sequence[0])
    total_distance = 0.0

    for t in range(len(result_sequence)):
        output = result_sequence[t]
        profile = profile_sequence[t]
        avg_distance_this_round = sum(kendall_tau_distance(output, voter) for voter in profile) / num_voters
        total_distance += avg_distance_this_round
    return total_distance / len(result_sequence)

def get_avg_sq_kt_distance(profile_sequence, result_sequence):
    num_voters = len(profile_sequence[0])
    total_distance = 0.0

    for t in range(len(result_sequence)):
        output = result_sequence[t]
        profile = profile_sequence[t]
        avg_distance_this_round = sum(squared_kendall_tau_distance(output, voter) for voter in profile) / num_voters
        total_distance += avg_distance_this_round
    return total_distance / len(result_sequence)

def get_egalitarian_kt_distance(profile_sequence, result_sequence):
    return np.max(get_avg_voter_distances(profile_sequence, result_sequence))

def get_standard_deviation_kt(profile_sequence, result_sequence):
    return np.std(get_avg_voter_distances(profile_sequence, result_sequence))

def get_proportionality_per_round():
    pass

def get_avg_voter_distances(profile_sequence, result_sequence):
    num_rounds = len(result_sequence)

    return get_voter_distances(profile_sequence, result_sequence) / num_rounds

def get_voter_distances(profile_sequence, result_sequence):
    num_voters = len(profile_sequence[0])
    num_rounds = len(result_sequence)
    voter_distances = np.zeros(num_voters)

    for t in range(num_rounds):
        output = result_sequence[t]
        profile = profile_sequence[t]
        for i, voter in enumerate(profile):
            voter_distances[i] += kendall_tau_distance(output, voter)

    return voter_distances