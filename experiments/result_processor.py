import numpy as np

from dspf_runner import kendall_tau_distance


def analyze_results(results):
    # call functions to get statistics
    # visualize
    pass

def get_perpetual_lower_quota_compliance(profile_sequence, result_sequence):
 #   num_voters = len(profile_sequence[0])
  #  num_rounds = len(result_sequence)

#    for t in range(len(result_sequence)):
 #       profile = profile_sequence[t]
  #      for voter in profile:
   #          is_
    
#    return / (num_voters * num_rounds)
     pass

def get_gini_influence_coefficient():
    pass

def get_avg_spearmans_footrule_distance(profile_sequence_list, output_ranking_list):
    # is it really necessary? Experiment and see
    pass

def get_avg_kt_distance(profile_sequence, result_sequence):
    num_voters = len(profile_sequence[0])
    total_distance = 0.0

    for t in range(len(result_sequence)):
        output = result_sequence[t]
        profile = profile_sequence[t]
        avg_distance_this_round = sum(kendall_tau_distance(output, voter) for voter in profile) / num_voters
        total_distance += avg_distance_this_round
    return total_distance / num_voters

def get_egalitarian_kt_distance(profile_sequence, result_sequence):
    return np.min(get_avg_voter_distances(profile_sequence, result_sequence))

def get_standard_deviation_kt(profile_sequence, result_sequence):
    return np.std(get_avg_voter_distances(profile_sequence, result_sequence))

def get_weird_proportionality():
    pass

def get_avg_voter_distances(profile_sequence, result_sequence):
    num_rounds = len(result_sequence)

    return get_avg_voter_distances(profile_sequence, result_sequence) / num_rounds

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