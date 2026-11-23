import pytest

def test_percentage():
    from math_toolkit import percentage

    assert percentage(50, 100) == 50
    assert percentage(1, 4) == 25
    with pytest.raises(ValueError):
        percentage(1, 0)

def test_percentage_change():
    from math_toolkit import percentage_change

    assert percentage_change(200, 150) == -25
    assert percentage_change(150, 200) == 33.33333333333333
    with pytest.raises(ValueError):
        percentage_change(0, 100)

def test_calculate_rate():
    from math_toolkit import calculate_rate

    assert calculate_rate(12000, 60) == 200
    with pytest.raises(ValueError):
        calculate_rate(100, 0)