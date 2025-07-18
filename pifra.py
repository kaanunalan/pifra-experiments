import argparse
import sys

from tspf_runner import run_tspf


def run_pifra(files, spf, update_function, initialization, threshold):
    results = [] # List of tuples of (profile, (result, satisfaction_matrix, support_matrix))
    profile_sequence_list = [[[[1, 0, 2, 3, 4], [2, 1, 0, 3, 4], [0, 2, 1, 3, 4]],[[1, 0, 2, 3, 4], [2, 1, 0, 3, 4], [0, 2, 1, 3, 4]]]]  # Placeholder for profile sequences
    
    for profile_sequence in profile_sequence_list:
        print(profile_sequence)
        results.append((profile_sequence, run_tspf(profile_sequence, spf, update_function, initialization, threshold)))
    
    print(results)
    #process_results(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        usage="%(prog)s [data.txt ...] --spf {kemeny,sq-kemeny,borda} "
                "--update {equal-weights,custom} --initialization {equal,custom}",
        description="Run a social choice algorithm with specified settings."
    )

    # Positional argument: one or more input files
    parser.add_argument("files", type=argparse.FileType("r"), nargs="*",
                        help="Zero or more input data files.")

    # Required options with limited choices
    parser.add_argument("--spf", choices=["borda", "kemeny", "sq-kemeny", "rsd"], required=False,
                        help="Social preference function.")
    parser.add_argument("--update", required=False,
                        help="Weight update function.")
    parser.add_argument("--initialization", choices=["equal", "special-voter-25-percent"], required=False,
                        help="Weight initialization method.")
    parser.add_argument("--threshold", type=int, required=False,
                        help="Satisfaction threshold value")

    args = parser.parse_args()

    # Now args.spf, args.update, args.initialization, and args.files are available
    # print("SPF:", args.spf)
    # print("Update function:", args.update)
    # print("Initialization method:", args.initialization)
    # print("Files:", [f.name for f in args.files])

    run_pifra(args.files, args.spf, args.update, args.initialization, args.threshold)

