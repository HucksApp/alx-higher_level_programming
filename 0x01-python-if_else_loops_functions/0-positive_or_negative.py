#!/usr/bin/python3
import random
number = random.randint(-10, 10)
fmt = "positive" if number > 0 else "negetive" if number < 0 else "zero"
print(f"{number} is {fmt}")
