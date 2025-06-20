import argparse
import sys

from data_generator import prepare_profiles
from dspf_runner import run_dspf
from result_processor import process_results


def run_pifra(files, spf, update_function, initialization):
    results = [] # List of tuples of (profile, result)
    profile_sequence_list = prepare_profiles()
    
    for profile_sequence in profile_sequence_list:
        results.append((profile_sequence, run_dspf(profile_sequence, spf, update_function, initialization)))
    
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
    parser.add_argument("--update", choices=["equal-weights", "custom"], required=False,
                        help="Weight update function.")
    parser.add_argument("--initialization", choices=["equal", "special-voter-absolute-majority"], required=False,
                        help="Weight initialization method.")

    args = parser.parse_args()

    # Now args.spf, args.update, args.initialization, and args.files are available
    print("SPF:", args.spf)
    print("Update function:", args.update)
    print("Initialization method:", args.initialization)
    print("Files:", [f.name for f in args.files])

    run_pifra(args.files, args.spf, args.update, args.initialization)

