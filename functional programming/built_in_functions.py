import itertools
import os
import random


# THE "map" FUNCTION
def upper(s):
    return s.upper()


# print(list(map(upper, ['sentence', 'fragment'])))
# print(list(map(lambda x: x.lower(), ['SENTENCE', 'FRAGMENT'])))

# You can of course achieve the same effect with a list comprehension
# print([upper(s) for s in ['SENTENCE', 'FRAGMENT']])

# THE "filter" FUNCTION
"""A predicate is a function that returns the truth value of some condition;
for use with filter(), the predicate must take a single value."""


def is_even(el):
    return (el % 2) == 0


# print(list(filter(is_even, range(10))))

# This can also be written as a list comprehension
# print(list(x for x in range(10) if is_even(x)))

# THE "enumerate" FUNCTION
"""
enumerate(iter, start=0) counts off the elements in the iterable returning 2-tuples containing the count (from
start) and each element.
"""
# for item in enumerate(['jobs', 'subject', 'verb', 'object', 'people', 'books', 'schools']):
#     print(item)

# enumerate() is often used when looping through a list and recording the
# indexes at which certain conditions are met

f = open('data.txt', 'r')
# for i, line in enumerate(f):
#     if line.strip() == '':
#         print('Blank line at line #%i' % i)

# print(dict(enumerate(f)))


# THE "sorted" FUNCTION
"""
sorted(iterable, key=None, reverse=False) collects all the elements of the iterable into a list, sorts
the list, and returns the sorted result. The key and reverse arguments are passed through to the constructed list’s sort()
method.
"""

rand_list = random.sample(range(10000), 8)
# print(rand_list)
# print(sorted(rand_list))
# print(sorted(rand_list, reverse=True))

# The any(iter) and all(iter) built-ins look at the truth values of an iterable’s contents.
# any() returns True if any element in the iterable is a true value, and all() returns True if all of the elements are true values
# print(any([0, 1, 0]))  # True
# print(any([0, 0, 0]))  # False
# print(any([1, 1, 1]))  # True
# print(all([0, 1, 0]))  # False
# print(all([0, 0, 0]))  # False
# print(all([1, 1, 1]))  # True


# zip(iterA, iterB, ...) takes one element from each iterable and returns them in a tuple
# It doesn’t construct an in-memory list and exhaust all the input iterators before returning; instead tuples are constructed
# and returned only if they’re requested. (The technical term for this behaviour is LAZY EVALUATION.)

it = zip(['a', 'b', 'c'], (1, 2, 3))
# print(it.__next__())


# THE "itertools" MODULE
"""
itertools.count(start, step) returns an infinite stream of evenly spaced values. You can optionally supply
the starting number, which defaults to 0, and the interval between numbers, which defaults to 1
"""
myiter = itertools.count()
myiter1 = itertools.count(20, 4)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
#
# print(next(myiter1))
# print(next(myiter1))

"""
itertools.cycle(iter) saves a copy of the contents of a provided iterable and returns a new iterator that returns
its elements from first to last. The new iterator will repeat these elements infinitely.
"""
mycycle = itertools.cycle([1, 2, 3, 4, 5])
# for x in range(12):
#     print(next(mycycle))

"""
itertools.repeat(elem, [n]) returns the provided element n times, or returns the element endlessly if n is
not provided.
"""
itert = itertools.repeat('abc', 5)

# for x in range(10):
#     print('{} - {}'.format(x, next(itert)))  # will throw a StopIteration exception a x = 5

"""
itertools.chain(iterA, iterB, ...) takes an arbitrary number of iterables as input, and returns all the
elements of the first iterator, then all the elements of the second, and so on, until all of the iterables have been exhausted.
"""

chain_iter = itertools.chain(['a', 'b', 'c'], (1, 2, 3))
# for x in range(6):
#     print('{} - {}'.format(x, next(chain_iter)))


"""
itertools.islice(iter, [start], stop, [step]) returns a stream that’s a slice of the iterator. With
a single stop argument, it will return the first stop elements. If you supply a starting index, you’ll get stop-start elements,
and if you supply a value for step, elements will be skipped accordingly. Unlike Python’s string and list slicing, you can’t
use negative values for start, stop, or step.

"itertools.islice(range(10), 8) =>
0, 1, 2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8) =>
2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8, 2) =>
2, 4, 6"
"""

myslice = itertools.islice(range(10), 8)
# for x in range(8):
#     print(next(myslice))

paths = itertools.starmap(os.path.join,
                          [('/bin', 'python'), ('/usr', 'bin', 'java'),
                           ('/usr', 'bin', 'perl'), ('/usr', 'bin', 'ruby')])
# print(next(paths))
# print(next(paths))
# print(next(paths))
# print(next(paths))

"""
itertools.filterfalse(predicate, iter) is the opposite of filter(), returning all elements for
which the predicate returns false.
"""
filterfalse_iter = itertools.filterfalse(is_even, itertools.count())

# for x in filterfalse_iter:
#     print(next(x))

"""
itertools.takewhile(predicate, iter) returns elements for as long as the predicate returns true. Once
the predicate returns false, the iterator will signal the end of its results
"""


def less_than_10(y):
    return y < 10


takewhile_iter = itertools.takewhile(less_than_10, itertools.count())  # => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

"""
itertools.dropwhile(predicate, iter) discards elements while the predicate returns true, and then returns the rest of the iterable’s results.
"""
itertools.dropwhile(less_than_10, itertools.count())  # 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...

itertools.dropwhile(is_even, itertools.count())  # => 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...

"""
itertools.compress(data, selectors) takes two iterators and returns only those elements of data for
which the corresponding element of selectors is true, stopping whenever either one is exhausted
"""

itertools.compress([1, 2, 3, 4, 5], [True, True, False, False, True])  # => 1, 2, 5

# COMBINATORIC FUNCTIONS
"""
The itertools.combinations(iterable, r) returns an iterator giving all possible r-tuple combinations of
the elements contained in iterable.
"""
itertools.combinations([1, 2, 3, 4, 5], 2)  # =>  (1, 2), (1, 3), (1, 4), (1, 5),
# (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)

itertools.combinations([1, 2, 3, 4, 5], 3)  # => (1, 2, 3), (1, 2, 4), (1, 2, 5),
# (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4),
# (2, 3, 5), (2, 4, 5), (3, 4, 5)

"""
The elements within each tuple remain in the same order as iterable returned them. For example, the number 1 is always before 2, 3, 4, or 5 in the examples above. A similar function, itertools.permutations(iterable,
r=None), removes this constraint on the order, returning all possible arrangements of length r:
"""

itertools.permutations([1, 2, 3, 4, 5], 2)  # (1, 2), (1, 3), (1, 4), (1, 5),
# (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2),
# (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5),
# (5, 1), (5, 2), (5, 3), (5, 4)

itertools.permutations([1, 2, 3, 4, 5])  # => (1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5),
# ...
# (5, 4, 3, 2, 1)

"""
If you don’t supply a value for r the length of the iterable is used, meaning that all the elements are permuted.
Note that these functions produce all of the possible combinations by position and don’t require that the contents of iterable
are unique:
"""

itertools.permutations('aba', 3)  # => ('a', 'b', 'a'), ('a', 'a', 'b'), ('b', 'a', 'a'),
# ('b', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'a')

"""
The itertools.combinations_with_replacement(iterable, r) function relaxes a different constraint: elements can be repeated within a single tuple. Conceptually an element is selected for the first position of
each tuple and then is replaced before the second element is selected.
"""
combinator = itertools.combinations_with_replacement([1, 2, 3, 4, 5], 2)  # (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
# (2, 2), (2, 3), (2, 4), (2, 5),
# (3, 3), (3, 4), (3, 5),
# (4, 4), (4, 5),
# (5, 5)

# for x in combinator:
#     print(x)


# GROUPING ELEMENTS
"""
The last function I’ll discuss, itertools.groupby(iter, key_func=None), is the most complicated.
key_func(elem) is a function that can compute a key value for each element returned by the iterable. If you don’t
supply a key function, the key is simply each element itself.
groupby() collects all the consecutive elements from the underlying iterable that have the same key value, and returns
a stream of 2-tuples containing a key value and an iterator for the elements with that key.
"""

city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
             ('Anchorage', 'AK'), ('Nome', 'AK'),
             ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'),
             ]


def get_state(city_state):
    return city_state[1]


state_group = itertools.groupby(city_list, get_state)  # =>
# ('AL', iterator-1),
# ('AK', iterator-2),
# ('AZ', iterator-3),
"""
where
iterator-1 =>
('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL')
iterator-2 =>
('Anchorage', 'AK'), ('Nome', 'AK')
iterator-3 =>
('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')
"""

for state in state_group:
    print(state[0])
    for x in state[1]:
        print(x[0], x)
    print()

"""
groupby() assumes that the underlying iterable’s contents will already be sorted based on the key. Note that the
returned iterators also use the underlying iterable, so you have to consume the results of iterator-1 before requesting
iterator-2 and its corresponding key.
"""
