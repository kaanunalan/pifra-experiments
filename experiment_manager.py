from itertools import product
from data_generator import generate_profile_sequence_list
from tspf_runner import run_tspf
from result_processor import get_avg_kt_distance, get_avg_spearman_footrule_distance, get_avg_sq_kt_distance, get_egalitarian_kt_distance, get_gini_influence_coefficient, get_perpetual_lower_quota_compliance, get_perpetual_lower_quota_compliance_ratio_special_voter, get_standard_deviation_kt, get_total_satisfaction_special_voter
from visualizer import visualize_all
import csv

def start_experiment(spf, update_function, initialization, threshold, profile_sequence_list):
    all_results = []         # list of result ranking lists per instance
    all_satisfaction = []    # list of satisfaction matrices per instance
    all_support = []         # list of support matrices per instance

    for profile_sequence in profile_sequence_list:
        results, satisfaction_matrix, support_matrix = run_tspf(
            profile_sequence, spf, update_function, initialization, threshold
        )
        all_results.append(results)
        all_satisfaction.append(satisfaction_matrix)
        all_support.append(support_matrix)
        
    # Calculate metrics for all instances (average over all profile sequences)
    sum_lower_quota = 0
    sum_gini = 0
    sum_avg_footrule = 0
    sum_avg_kt = 0
    sum_std_kt = 0
    sum_egalitarian_kt = 0    
    sum_total_sat = 0
    sum_avg_sq_kt = 0
    for results, sat_matrix, support_matrix, profile_sequence in zip(all_results, all_satisfaction, all_support, profile_sequence_list):
        sum_lower_quota += get_perpetual_lower_quota_compliance(satisfaction_matrix, support_matrix)
        sum_gini += get_gini_influence_coefficient(profile_sequence, results, sat_matrix)
        sum_avg_footrule += get_avg_spearman_footrule_distance(profile_sequence, results)
        sum_avg_kt += get_avg_kt_distance(profile_sequence, results)
        sum_std_kt += get_standard_deviation_kt(profile_sequence, results)
        sum_egalitarian_kt += get_egalitarian_kt_distance(profile_sequence, results)
        sum_total_sat += get_total_satisfaction_special_voter(satisfaction_matrix, support_matrix)
        sum_avg_sq_kt += get_avg_sq_kt_distance(profile_sequence, results)
    avg_lower_quota = sum_lower_quota / len(profile_sequence_list)
    avg_gini = sum_gini / len(profile_sequence_list)
    avg_footrule = sum_avg_footrule / len(profile_sequence_list)
    avg_kt = sum_avg_kt / len(profile_sequence_list)
    std_kt = sum_std_kt / len(profile_sequence_list)
    egalitarian_kt = sum_egalitarian_kt / len(profile_sequence_list)
    avg_total_sat = sum_total_sat / len(profile_sequence_list)
    avg_sq_kt = sum_avg_sq_kt / len(profile_sequence_list)
    return (
    (spf, update_function, initialization, threshold, avg_lower_quota),
    (spf, update_function, initialization, threshold, avg_gini),
    (spf, update_function, initialization, threshold, avg_footrule),
    (spf, update_function, initialization, threshold, avg_kt),
    (spf, update_function, initialization, threshold, std_kt),
    (spf, update_function, initialization, threshold, egalitarian_kt),
    (spf, update_function, initialization, threshold, avg_total_sat),
    (spf, update_function, initialization, threshold, avg_sq_kt)
    )

if __name__ == "__main__":
    spf_list = ["borda", "kemeny", "sq-kemeny", "weighted-rsd"]
    update_functions = [
        "constant", "myopic-kt", "myopic-sq-kt", "kt", "sq-kt",
        "unit-cost", "kt-reset", "unit-cost-reset",
        "perpetual-kt", "myopic-kt-special-voter", "kt-special-voter"
    ]
    initializations = ["equal", "special-voter-25-percent"]
    thresholds = [0, 3, 7] # 10 is maximal KT distance for 5 alternatives
    profile_sequence_list = generate_profile_sequence_list()

    # Write profile sequences to a file for reproducibility
    with open("profile_sequences.txt", 'w') as f:
        for i, profile_sequence in enumerate(profile_sequence_list):
            f.write(f"Profile Sequence {i+1}:\n")
            for profile in profile_sequence:
                f.write(f"{profile}\n")
            f.write("\n")

    # Store metrics for each configuration
    gini_values = []
    lower_quota_values = []
    avg_footrule_values = []
    avg_kt_values = []
    std_kt_values = []
    egalitarian_kt_values = []
    total_sats_special_voter = []
    avg_sq_kt_values = []
    for spf, update_func, init, threshold in product(spf_list, update_functions, initializations, thresholds):
        print(f"Running experiment with SPF: {spf}, Update Function: {update_func}, Initialization: {init}, Threshold: {threshold}")
        avg_lower_quota, avg_gini, avg_footrule, avg_kt, std_kt, egalitarian_kt, total_sat, avg_sq_kt = start_experiment(spf, update_func, init, threshold, profile_sequence_list)
        lower_quota_values.append(avg_lower_quota)
        gini_values.append(avg_gini)
        avg_footrule_values.append(avg_footrule)
        avg_kt_values.append(avg_kt)
        std_kt_values.append(std_kt)
        egalitarian_kt_values.append(egalitarian_kt)
        total_sats_special_voter.append(total_sat)
        avg_sq_kt_values.append(avg_sq_kt)

    visualize_all(
        spf_list, update_functions, lower_quota_values, gini_values,
        avg_footrule_values, avg_kt_values, std_kt_values, egalitarian_kt_values, 
        total_sats_special_voter, avg_sq_kt_values
    )

    # Save results to a csv file for each metric
    with open("experiment_results.csv", 'w', newline='') as csvfile:
        fieldnames = ["SPF", "Update Function", "Initialization", "Threshold",
                      "Avg Lower Quota", "Avg Gini", "Avg Footrule",
                      "Avg KT", "Std KT", "Egalitarian KT",
                      "Total Number of Satisfaction Special Voter", "Avg SQ KT"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        
        for (spf, update_func, init, threshold), lower_quota, gini, footrule, kt, std_kt, egalitarian_kt, total_sats_special_voter, avg_sq_kt in zip(
            product(spf_list, update_functions, initializations, thresholds),
            lower_quota_values, gini_values, avg_footrule_values,
            avg_kt_values, std_kt_values, egalitarian_kt_values,
            total_sats_special_voter, avg_sq_kt_values
        ):
            writer.writerow({
                'SPF': spf,
                'Update Function': update_func,
                'Initialization': init,
                'Threshold': threshold,
                'Avg Lower Quota': lower_quota,
                'Avg Gini': gini,
                'Avg Footrule': footrule,
                'Avg KT': kt,
                'Std KT': std_kt,
                'Egalitarian KT': egalitarian_kt,
                'Total Number of Satisfaction Special Voter': total_sats_special_voter,
                'Avg SQ KT': avg_sq_kt
            })
    