from fb import *

def test_multiple_of_three():
    assert fb(6) == "Fizz"

def test_multiple_of_five():
    assert fb(55) == "Buzz"

def test_multiple_of_three_and_five():
    assert fb(90) == "FizzBuzz"

def test_not_a_multiple_of_three_or_five():
    assert fb(62) == 62