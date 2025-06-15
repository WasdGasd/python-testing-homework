from average import calculate_average

def test_average_positive():
    assert calculate_average([1, 2, 3, 4]) == 3

def test_average_negative():
    assert calculate_average([-5, -10, -15]) == -10

def test_average_empty():
    assert calculate_average([]) is None
