import pytest
from algorithms.eproximator import run_hill_climber
import math

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
    approximation, b, c = run_hill_climber(e, 0, 0)
    assert approximation == e
    assert b == ["+"]

def test_subtraction(e):
    approximation, b, c = run_hill_climber(-e, 0, 0)
    assert approximation == -e
    assert b == ["-"]

def test_multiplication(e):
    approximation, b, c = run_hill_climber(e, 1, 0)
    assert approximation == e
    assert b == ["*"]

def test_division(e):
    approximation, b, c = run_hill_climber(1, e, 0)
    assert approximation == 1
    assert b == ["/"]

def test_power(e_to_the_e, e):
    approximation, b, c = run_hill_climber(e_to_the_e, e, 0)
    assert approximation == e_to_the_e
    assert b == ["^e"]


def test_root(e_root_e, e):
    approximation, b, c = run_hill_climber(e_root_e, e, 0)
    assert approximation == e_root_e
    assert b == ["^1/e"]

def test_log(arbitrary_natural_log):
    approximation, b, c = run_hill_climber(arbitrary_natural_log, 20, 0)
    assert approximation == arbitrary_natural_log
    assert b == ["ln"]
