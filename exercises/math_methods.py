import random

# generate list of 20 random numbers btw 0 & 49
random_nums = [random.randrange(0, 49) for n in range(20)]
print(random_nums)

# build a new list that contains each number squared
squared_nums = [num**2 for num in random_nums]
print(squared_nums)
