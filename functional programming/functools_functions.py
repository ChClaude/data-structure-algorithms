import functools
import itertools
import operator


def log(message, subsystem):
    """Write the contents of message to the specified subsystem."""
    print('%s: %s' % (subsystem, message))


server_log = functools.partial(log, subsystem='server')
# server_log('Unable to open socket')

"""
functools.reduce(func, iter, [initial_value]) cumulatively performs an operation on all the iterable’s elements and, therefore, can’t be applied to infinite iterables. func must be a function that takes two elements
and returns a single value. functools.reduce() takes the first two elements A and B returned by the iterator and calculates func(A, B). It then requests the third element, C, calculates func(func(A, B), C), combines this result with the fourth element returned, and continues until the iterable is exhausted. If the iterable returns
no values at all, a TypeError exception is raised. If the initial value is supplied, it’s used as a starting point and
func(initial_value, A) is the first calculation.
"""

# print(functools.reduce(operator.concat, ['A', 'BB', 'C']))  # ABBC
# print(functools.reduce(operator.mul, [1, 2, 3], 1))  # 6
# print(functools.reduce(operator.mul, [], 1))  # 1

# If you use operator.add() with functools.reduce(), you’ll add up all the elements of the iterable. This case
# is so common that there’s a special built-in called sum() to compute it:
# print(functools.reduce(operator.add, [1, 2, 3, 4], 0))  # 10
# print(sum([1, 2, 3, 4]))  # 10

# Instead of:
# product = functools.reduce(operator.mul, [1, 2, 3], 1)

# You can write:
# product = 1
# for i in [1, 2, 3]:
#     product *= i

"""
A related function is itertools.accumulate(iterable, func=operator.add). It performs the same
calculation, but instead of returning only the final result, accumulate() returns an iterator that also yields each partial
result
"""

itertools.accumulate([1, 2, 3, 4, 5])  # => 1, 3, 6, 10, 15
itertools.accumulate([1, 2, 3, 4, 5], operator.mul)  # => 1, 2, 6, 24, 120

items = [(1, 5), (2, 4), (7, 4), (8, 5), (1, 9), (2, 9)]
total = [b for a, b in items]

print(total)
