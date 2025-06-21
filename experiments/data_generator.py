from prefsampling.ordinal import euclidean
from prefsampling.core.euclidean import EuclideanSpace

def prepare_profiles():
    """
    Generates data to be used in the experiments.

    Returns a list of preference profiles.
    """
    profiles_list = []
    profiles_list.append(generate_profile_sequence())
    return profiles_list

def generate_profile_sequence():
    profile_sequence = []
    profile_sequence.append(generate_euclidean(5, 3, 2))
    return profile_sequence

def generate_euclidean(num_voters, num_candidates, num_dimensions):
    # Generate voter and candidate positions in 2D
    profile = euclidean(
        num_voters=num_voters,
        num_candidates=num_candidates,
        num_dimensions=num_dimensions,
        voters_positions=EuclideanSpace.UNIFORM_BALL,
        candidates_positions=EuclideanSpace.UNIFORM_BALL
    )
    
    return profile