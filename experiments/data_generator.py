from prefsampling.ordinal import euclidean
from prefsampling.core.euclidean import EuclideanSpace

def generate_profile_sequence_list():
    """
    Generates data to be used in the experiments.

    Returns a list of preference profiles.
    """
    profiles_list = []
    profiles_list.append(generate_euclidean_profile_sequence())
    return profiles_list

def generate_euclidean_profile_sequence():
    profile_sequence = []

    profile_sequence.append(generate_euclidean(50, 5, 2, 1))
    profile_sequence.append(generate_euclidean(50, 5, 2, 2))
    profile_sequence.append(generate_euclidean(50, 5, 2, 3))
    profile_sequence.append(generate_euclidean(50, 5, 2, 4))
    profile_sequence.append(generate_euclidean(50, 5, 2, 5))
    profile_sequence.append(generate_euclidean(50, 5, 2, 6))
    profile_sequence.append(generate_euclidean(50, 5, 2, 7))
    profile_sequence.append(generate_euclidean(50, 5, 2, 8))
    profile_sequence.append(generate_euclidean(50, 5, 2, 9))
    profile_sequence.append(generate_euclidean(50, 5, 2, 10))

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