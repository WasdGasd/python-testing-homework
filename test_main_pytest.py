import pytest
from main import calculate_average

def test_positive_numbers():
    assert calculate_average([10, 20, 30]) == 20

def test_mixed_numbers():
    assert calculate_average([-5, 0, 5]) == 0

def test_empty_list():
    assert calculate_average([]) is None
