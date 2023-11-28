#!/usr/bin/python3

def fizzbuzz() -> None:
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            ret = "FizzBuzz"
        elif num % 3 == 0:
            ret = "Fizz"
        elif num % 5 == 0:
            ret = "Buzz"
        else:
            ret = num
        print(f"{ret} ", end='')
