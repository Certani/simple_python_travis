# a minimal pytest example from pytest

# this function will be tested
def func(x):
    return x + 1

# we assume if we enter 4 the return value will be 5
def test_answer():
    assert func(4) == 5

