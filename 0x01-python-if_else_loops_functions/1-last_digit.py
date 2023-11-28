#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
gr = "greater than 5"
lss = "less than 6 and not 0"
lst = number % 10 if number >= 0 else (-number % 10) * -1
fmt = gr if lst > 5 else lss if lst < 6 and lst != 0 else "0"
print(f"Last digit of {number} is {lst} and is {fmt}")
