import math
import random

import numpy as np
import pytest

from tspf_runner import (
    initialize_weights,
    run_weighted_borda,
    run_weighted_kemeny,
    run_random_serial_dictatorship,
    run_weighted_random_serial_dictatorship,
    compute_satisfaction
)

# ----------------------------
# Test data: rankings and weihgts
# ----------------------------

@pytest.fixture
def profile_1():
    return [[0, 1, 2], [1, 0, 2], [1, 0, 2], [2, 0, 1], [2, 1, 0]]

@pytest.fixture
def weights_equal():
    return np.ones(5)

# ----------------------------
# Weight initialization tests
# ----------------------------

def test_initialize_weights_equal(profile_1):
    w = initialize_weights([profile_1], initialization="equal")
    assert np.all(w == np.array([1, 1, 1, 1, 1]))

def test_initialize_weights_special(profile_1):
    w = initialize_weights([profile_1], initialization="special-voter-25-percent")
    # for 2 voters, three_quarter_total_weight = 1
    # special voter gets ceil(1/3) = 1, so weights = [1,1]
    assert np.all(w == np.array([1, 1, 1, 1, 2]))

# ----------------------------
#  Weighted Borda tests
# ----------------------------

def test_run_weighted_borda(profile_1, weights_equal):
    out = run_weighted_borda(profile_1, weights_equal)
    assert out == [1, 0, 2]

def test_run_weighted_borda_custom(profile_1):
    w = np.array([1, 1, 1, 3, 1])
    out = run_weighted_borda(profile_1, w)
    assert out == [2, 0, 1]

# ----------------------------
#  Weighted Kemeny tests
# ----------------------------

def test_run_weighted_kemeny(profile_1, weights_equal):
    out = run_weighted_kemeny(profile_1, weights_equal, squared_kemeny=False)
    assert out == [1, 0, 2]

def test_run_weighted_sq_kemeny(profile_1, weights_equal):
    out = run_weighted_kemeny(profile_1, weights_equal, squared_kemeny=True)
    assert out == [1, 2, 0]

def test_run_weighted_kemeny_2(weights_equal):
    profile_2 = [[1, 0, 2], [1, 0, 2], [0, 2, 1]]
    out = run_weighted_kemeny(profile_2, weights_equal, squared_kemeny=False)
    assert out == [1, 0, 2]

def test_run_weighted_sq_kemeny_2(weights_equal):
    profile_2 = [[1, 0, 2], [1, 0, 2], [0, 2, 1]]
    out = run_weighted_kemeny(profile_2, weights_equal, squared_kemeny=True)
    assert out == [0, 1, 2]

def test_run_weighted_kemeny_3():
    w = np.array([1, 1, 5])
    profile_2 = [[1, 0, 2], [1, 0, 2], [0, 2, 1]]
    out = run_weighted_kemeny(profile_2, w, squared_kemeny=False)
    assert out == [0, 2, 1]

def test_run_weighted_sq_kemeny_3():
    w = np.array([1, 1, 5])
    profile_2 = [[1, 0, 2], [1, 0, 2], [0, 2, 1]]
    out = run_weighted_kemeny(profile_2, w, squared_kemeny=True)
    assert out == [0, 1, 2]

# ----------------------------
#  Random serial dictatorship
# ----------------------------

def test_run_random_serial_dictatorship(profile_1):
    out = run_random_serial_dictatorship(profile_1)
    assert out in profile_1

def test_run_weighted_random_serial_dictatorship(profile_1):
    out = run_weighted_random_serial_dictatorship(profile_1, [0,0,1,0,0])
    assert out == [1, 0, 2]

def test_compute_satisfaction_all_true():
    seq = [[[0,1],[1,0]], [[0,1],[1,0]]]
    out = [ [0,1] , [0,1] ] 
    mat = compute_satisfaction(seq, out, threshold=0)
    assert mat == [[1,0],[1,0]]
