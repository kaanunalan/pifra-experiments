from prefsampling.ordinal import euclidean
from prefsampling.core.euclidean import EuclideanSpace


def generate_profile_sequence_list():
    """
    Generates data (list of profile sequences) to be used in the experiments.

    :return: List of preference profiles.
    """
    profiles_list = []
    for i in range(30):
        profiles_list.append(generate_euclidean_profile_sequence(i * 30 + 1))
    return profiles_list

def generate_euclidean_profile_sequence(start_seed):
    profile_sequence = []

    for seed in range(start_seed, start_seed + 30):
        profile_sequence.append(generate_euclidean(50, 5, 2, seed))

    return profile_sequence

def generate_euclidean(num_voters, num_candidates, num_dimensions, seed):
    # Generate voter and candidate positions in 2D
    profile = euclidean(
        num_voters=num_voters,
        num_candidates=num_candidates,
        num_dimensions=num_dimensions,
        voters_positions=EuclideanSpace.UNIFORM_BALL,
        candidates_positions=EuclideanSpace.UNIFORM_BALL,
        seed=seed
    )
    
    return profile