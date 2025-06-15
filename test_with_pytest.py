def multiply(a, b):
    return a * b

def test_multiply_positive():
    assert multiply(4, 5) == 20

def test_multiply_zero():
    assert multiply(0, 10) == 0
