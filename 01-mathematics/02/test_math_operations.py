import pytest

from math_operations import (
    power,
    square_root,
    logarithm,
    scientific_notation
)

def test_power():
    assert(power(2, 3) == 8)
    assert(power(5, 0) == 1)
    assert(power(3, 2) == 9)

def test_square_root():
    assert(square_root(4) == 2)
    assert(square_root(9) == 3)
    with pytest.raises(ValueError):
        square_root(-1)

def test_logarithm():
    assert(logarithm(1) == 0)
    assert(logarithm(8, 2) == 3)
    with pytest.raises(ValueError):
        logarithm(-1)
    with pytest.raises(ValueError):
        logarithm(1, 1)
    with pytest.raises(ValueError):
        logarithm(1, -2)

def test_scientific_notation():
    assert(scientific_notation(1000) == "1.000000e+03")
    assert(scientific_notation(0.001) == "1.000000e-03")