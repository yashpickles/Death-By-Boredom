# Take two lists, say for example these two:

# and write a program that returns a list that contains only the elements that are common between the lists (without
# duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using
# at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7). The original formulation of
# this exercise said to write the solution using one line of Python, but a few readers pointed out that this was
# impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the
# original directive and read about the set command in Python 3.3, or try to implement this on your own and use at
# least one list comprehension in the solution. Extra: Randomly generate two lists to test this


def intersection(a, b):
    c = [num for num in set(a) if num in b]
    return c


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(intersection(a, b))

#EXTRA!
def intersectionextra(d, e):
    f = [ele for ele in set(d) if ele in e ]
    return f

import random

d = random.sample(range(1, 30), 13)
e = random.sample(range(1, 45), 15)
print(intersectionextra(d, e))

