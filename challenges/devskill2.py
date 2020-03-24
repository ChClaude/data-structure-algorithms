mylist = [1, 4, 5, 6, 18, 13, 15]
mydictionary = {"claude": {"name": "Claude", "age": 15}, "martin": {"name": "Martin", "age": 35}}
mytuple = (1, 4, 5, 6)
myset = {1, 2, 5, 4}


# print(type(mylist))
# print(type(mydictionary))
# print(type(mytuple))
# print(type(myset))

# Linear search
def linear_search(data, target):
    for el in data:
        if el == target:
            return "found"

    return "not found"


# found 8 in mylist
# print(linear_search(mylist, 18))

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor


# scale(mylist, 2)
# print(mylist)
# print(sum(mylist))
# print(sorted(mylist))
# print('maroon', 5)
# print('a', 'b', 'c', sep=' : ')

# reply = input("Enter x and y, separated by spaces:")
# pieces = reply.split()  # returns a list of strings, as separated by spaces
# x = float(pieces[0])
# y = float(pieces[1])

# file = open("Test.txt")
# print(file.read())

output = open('output.txt', 'w')
# output.write(str(mylist))

# print(mydictionary, file=output)


# Generators
def factors(n):  # generator that computes factors
    k = 1
    while k * k < n:  # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:  # special case if n is perfect square
        yield k


for x in factors(100):
    print(x)


def fibonacci(n):
    a = 0
    b = 1
    while a < n:  # keep going...
        yield a  # report value, a, during this pass
        future = a + b
        a = b  # this will be next value reported
        b = future  # and subsequently this


# for x in fibonacci(52):
#     print(x)
