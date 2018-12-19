def fizzbuzz():
    for num in range(1,101):
        print(
            {
                num % 3 == 0 and num % 5 != 0 : "Fizz",
                num % 5 == 0 and num % 3 != 0 : "Buzz",
                num % 5 == 0 and num % 3 == 0 : "FizzBuzz",
            }.get(True, num)
        )

fizzbuzz()