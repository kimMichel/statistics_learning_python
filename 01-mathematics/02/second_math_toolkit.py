
import math


def square_values(values):
    return [x ** 2 for x in values]


def population_standard_deviation(values):
    if not values:
        raise ValueError("Values cannot be empty")

    mean = sum(values) / len(values)

    squared_deviations = [
        (x - mean) ** 2 for x in values
    ]

    variance = sum(squared_deviations) / len(values)

    return math.sqrt(variance)


def logarithm(value, base):
    if value <= 0:
        raise ValueError("Logarithm value must be positive")

    if base <= 0 or base == 1:
        raise ValueError(
            "Logarithm base must be positive and not equal to 1"
        )

    return math.log(value, base)


def convert_to_scientific_notation(number):
    return f"{number:.6e}"
