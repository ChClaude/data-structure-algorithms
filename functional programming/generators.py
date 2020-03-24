def generate_ints(N):
    for i in range(N):
        yield i


gen = generate_ints(3)


# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))  # This statement throws a StopIteration exception


# A recursive generator that generates Tree leaves in in-order.
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x
    yield t.label
    for x in inorder(t.right):
        yield x


def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1


it = counter(10)  # doctest: +SKIP

print(next(it))
print(next(it))
print(it.send(8))
print(next(it))
# print(next(it))  # this will throw a StopIteration Exception
