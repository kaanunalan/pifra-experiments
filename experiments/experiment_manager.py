from itertools import product
from experiments.data_generator import generate_profile_sequence_list
from dspf_runner import run_dspf


def start_experiment(spf, update_function, initialization, threshold, profile_sequence_list):
    results = [] # List of tuples of (profile, result)
    
    for profile_sequence in profile_sequence_list:
        results.append((profile_sequence, run_dspf(profile_sequence, spf, update_function, initialization, threshold)))
    
    return results

if __name__ == "__main__":
    spf_list = ["borda", "kemeny", "sq-kemeny", "rsd"]
    update_functions = [
        "constant", "myopic-kt", "myopic-sq-kt", "kt", "sq-kt",
        "unit-cost", "kt-reset", "unit-cost-reset",
        "special-voter-kt", "perpetual-kt", "perpetual-nash"
    ]
    initializations = ["equal", "special-voter-25-percent"]
    thresholds = [0, 5, 10, 100]
    profile_sequence_list = generate_profile_sequence_list()
    for spf, update_func, init, threshold in product(spf_list, update_functions, initializations, thresholds):
        results = start_experiment(spf, update_func, init, threshold, profile_sequence_list)
        analyze_results(results)
