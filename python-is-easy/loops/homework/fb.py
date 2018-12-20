def fb(n):
    """ Testable version of FizzBuzz (no side effects)
    """
    return {
        n % 3 == 0 and n % 5 != 0 : "Fizz",
        n % 5 == 0 and n % 3 != 0 : "Buzz",
        n % 3 == 0 and n % 5 == 0 : "FizzBuzz"
    }.get(True, n)