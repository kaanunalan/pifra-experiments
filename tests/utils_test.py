import pytest

from utils import kendall_tau_distance, squared_kendall_tau_distance, spearman_footrule_distance, is_satisfied

# ----------------------------
# Test data: rankings
# ----------------------------

@pytest.fixture
def identity_ranking():
    return [0, 1, 2, 3]

@pytest.fixture
def reverse_ranking():
    return [3, 2, 1, 0]

@pytest.fixture
def swap_first_two():
    return [1, 0, 2, 3]

# ----------------------------
# Kendall tau distance tests
# ----------------------------

def test_kendall_identity(identity_ranking):
    # identical rankings => distance 0
    assert kendall_tau_distance(identity_ranking, identity_ranking) == 0

def test_kendall_reverse(identity_ranking, reverse_ranking):
    # all pairs inverted: n=4 => max distance = 6 pairs
    assert kendall_tau_distance(identity_ranking, reverse_ranking) == 6

def test_kendall_one_swap(identity_ranking, swap_first_two):
    # only pair (0,1) inverted => distance 1
    assert kendall_tau_distance(identity_ranking, swap_first_two) == 1

def test_kendall_commutative(identity_ranking, swap_first_two):
    # symmetry: d(r1,r2) == d(r2,r1)
    d1 = kendall_tau_distance(identity_ranking, swap_first_two)
    d2 = kendall_tau_distance(swap_first_two, identity_ranking)
    assert d1 == d2

# ----------------------------
# Squared Kendall tau distance tests
# ----------------------------

def test_squared_kendall_zero(identity_ranking):
    # 0^2 == 0
    assert squared_kendall_tau_distance(identity_ranking, identity_ranking) == 0

def test_squared_kendall_positive(identity_ranking, swap_first_two):
    # 1^2 == 1
    assert squared_kendall_tau_distance(identity_ranking, swap_first_two) == 1

# ----------------------------
# Spearman's footrule distance tests
# ----------------------------

def test_spearman_identity(identity_ranking):
    assert spearman_footrule_distance(identity_ranking, identity_ranking) == 0

def test_spearman_simple_swap(identity_ranking, swap_first_two):
    # positions of 0 and 1 swapped by 1 each => total distance 2
    # |pos1(0)-pos2(0)| + |pos1(1)-pos2(1)| = |0-1| + |1-0| = 1+1 = 2
    assert spearman_footrule_distance(identity_ranking, swap_first_two) == 2

def test_spearman_reverse(identity_ranking, reverse_ranking):
    # for n=4, max footrule dist. = sum |i-(3-i)| = |0-3|+|1-2|+|2-1|+|3-0| = 3+1+1+3 = 8
    assert spearman_footrule_distance(identity_ranking, reverse_ranking) == 8

# ----------------------------
# is_satisfied tests
# ----------------------------

def test_is_satisfied_exact(identity_ranking):
    # distance = 0, default threshold 0 => satisfied
    assert is_satisfied(identity_ranking, identity_ranking) is True

def test_is_satisfied_below_threshold(identity_ranking, swap_first_two):
    # distance = 1, threshold = 1 => satisfied
    assert is_satisfied(identity_ranking, swap_first_two, threshold=1) is True

def test_is_not_satisfied_above_threshold(identity_ranking, swap_first_two):
    # distance = 1, threshold = 0 => not satisfied
    assert is_satisfied(identity_ranking, swap_first_two, threshold=0) is False

