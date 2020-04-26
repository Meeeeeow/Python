#exercise
from functools import reduce


# 1 Capitalize all of the pet names and print the list
def capitalpets(item):
    return item.title()


my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(capitalpets, my_pets)))


def passing(item):
    return item > 50


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(passing, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


li = []
li = my_numbers + scores
print(reduce(accumulator, li, 0))