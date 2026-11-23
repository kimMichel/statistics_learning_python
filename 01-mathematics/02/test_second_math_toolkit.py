
import pytest

from second_math_toolkit import (
    square_values,
    population_standard_deviation,
    logarithm,
    convert_to_scientific_notation
)


def test_square_values():
    assert square_values([10, 12, 14, 16, 18]) == [
        100, 144, 196, 256, 324
    ]


def test_population_standard_deviation():
    result = population_standard_deviation(
        [10, 12, 14, 16, 18]
    )

    assert result == pytest.approx(2.8284271247461903)


def test_population_standard_deviation_empty_list():
    with pytest.raises(ValueError):
        population_standard_deviation([])


def test_logarithm():
    assert logarithm(1024, 2) == pytest.approx(10)


@pytest.mark.parametrize(
    "value, base",
    [
        (0, 2),
        (-10, 2),
        (10, 0),
        (10, 1),
        (10, -2),
    ]
)
def test_logarithm_invalid_arguments(value, base):
    with pytest.raises(ValueError):
        logarithm(value, base)


def test_convert_to_scientific_notation():
    assert convert_to_scientific_notation(125000000) == "1.250000e+08"
    assert convert_to_scientific_notation(0.00000042) == "4.200000e-07"
