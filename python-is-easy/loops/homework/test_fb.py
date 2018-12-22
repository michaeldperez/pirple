from fb import *
import pytest

@pytest.mark.parametrize("input, expected", [
    (6, "Fizz"),
    (55, "Buzz"),
    (90, "FizzBuzz"),
    (62, 62)
])
def test_fizzbuzz(input, expected):
    assert fb(input) == expected