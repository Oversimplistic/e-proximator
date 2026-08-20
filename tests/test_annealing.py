import pytest
import math

from algorithms.simulated_annealing_algorithm import run_simulated_annealing

TOL = 1e-1


@pytest.fixture
def e():
    return math.e

@pytest.fixture
def e_squared():
    return math.e**2

@pytest.fixture
def e_to_the_e():
    return math.e**math.e

@pytest.fixture
def e_root_e():
    return math.e ** (1/math.e)

@pytest.fixture
def arbitrary_natural_log():
    return math.log(20, math.e)


def test_addition(e):
    path, approximation, steps, error = run_simulated_annealing(e, 0)
    assert approximation == pytest.approx(e, abs=TOL)
    assert error < TOL
    assert len(path) > 0

def test_subtraction(e):
    path, approximation, steps, error = run_simulated_annealing(-e, 0)
    assert approximation == pytest.approx(-e, abs=TOL)
    assert error < TOL
    assert len(path) > 0

def test_multiplication(e):
    path, approximation, steps, error = run_simulated_annealing(e, 1)
    assert approximation == pytest.approx(e, abs=TOL)
    assert error < TOL
    assert len(path) > 0

def test_division(e):
    path, approximation, steps, error = run_simulated_annealing(1, e)
    assert approximation == pytest.approx(1, abs=TOL)
    assert error < TOL
    assert len(path) > 0

def test_power(e_to_the_e, e):
    path, approximation, steps, error = run_simulated_annealing(e_to_the_e, e)
    assert approximation == pytest.approx(e_to_the_e, abs=TOL)
    assert error < TOL
    assert len(path) > 0

def test_root(e_root_e, e):
    path, approximation, steps, error = run_simulated_annealing(e_root_e, e)
    assert approximation == pytest.approx(e_root_e, abs=TOL)
    assert error < TOL
    assert len(path) > 0

def test_log(arbitrary_natural_log):
    path, approximation, steps, error = run_simulated_annealing(arbitrary_natural_log, 20)
    assert approximation == pytest.approx(arbitrary_natural_log, abs=TOL)
    assert error < TOL
    assert len(path) > 0