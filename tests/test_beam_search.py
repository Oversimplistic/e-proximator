import pytest
from algorithms.beam_search_algorithm import beamSearch
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
    path, approximation, error = beamSearch(e, 0)
    assert approximation == e
    assert path == ["+"]

def test_subtraction(e):
    path, approximation, error = beamSearch(-e, 0)
    assert approximation == -e
    assert path == ["-"]

def test_multiplication(e):
    path, approximation, error = beamSearch(e, 1)
    assert approximation == e
    assert path == ["*"]

def test_division(e):
    path, approximation, error = beamSearch(1, e)
    assert approximation == 1
    assert path == ["/"]

def test_power(e_to_the_e, e):
    path, approximation, error = beamSearch(e_to_the_e, e)
    assert approximation == e_to_the_e
    assert path == ["^e"]


def test_root(e_root_e, e):
    path, approximation, error = beamSearch(e_root_e, e)
    assert approximation == e_root_e
    assert path == ["^1/e"]

def test_log(arbitrary_natural_log):
    path, approximation, error = beamSearch(arbitrary_natural_log, 20)
    assert approximation == arbitrary_natural_log
    assert path == ["ln"]
