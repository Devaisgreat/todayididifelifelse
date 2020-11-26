import random

random_integer = random.randint(1, 10)
print(random_integer)

# 0.0000000 - 0.99999999....
random_float = random.random()
print(random_float)

random_float * 5
# 0.00000 - 4.999999999.....

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
