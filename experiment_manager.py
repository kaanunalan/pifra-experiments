from itertools import product
from data_generator import generate_profile_sequence_list
from tspf_runner import run_tspf
from result_processor import analyze_results


def start_experiment(spf, update_function, initialization, threshold, profile_sequence_list):
    all_results = []         # list of result rankings per experiment
    all_satisfaction = []    # list of satisfaction matrices per experiment
    all_support = []         # list of support  matrices per experiment

    for profile_sequence in profile_sequence_list:
        results, satisfaction_matrix, support_matrix = run_tspf(
            profile_sequence, spf, update_function, initialization, threshold
        )
        all_results.append(results)
        all_satisfaction.append(satisfaction_matrix)
        all_support.append(support_matrix)

    return all_results, all_satisfaction, all_support

if __name__ == "__main__":
    spf_list = ["borda", "kemeny", "sq-kemeny", "rsd", "weighted-rsd"]
    update_functions = [
        "constant", "myopic-kt", "myopic-sq-kt", "kt", "sq-kt",
        "unit-cost", "kt-reset", "unit-cost-reset",
        "special-voter-kt", "perpetual-kt", "perpetual-nash"
    ]
    initializations = ["equal", "special-voter-25-percent"]
    thresholds = [0, 3, 7] # 10 is maximal KT distance for 5 alternatives
    profile_sequence_list = generate_profile_sequence_list()
    for spf, update_func, init, threshold in product(spf_list, update_functions, initializations, thresholds):
        all_results, all_satisfaction, all_support = start_experiment(spf, update_func, init, threshold, profile_sequence_list)
        print(all_results)
        print("--------------------")
        print(all_satisfaction)
        print("--------------------")
        print(all_support)
        for results, sat_matrix, support_matrix in zip(all_results, all_satisfaction, all_support):
            for profile_sequence in profile_sequence_list:
                analyze_results(profile_sequence, results, sat_matrix, support_matrix)
