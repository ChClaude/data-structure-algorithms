# for x, y in [(3, 9), (2, 1), (5, 8), (4, 6)]:
#     print("x = %s; y = %s" % (x, y))

mydict = {"CG": "Congo", "FR": "France", "USA": "United Sates of America", "DRC": "Democratic Rep of Congo"}

# for key, value in mydict.items():
#     print('Key = %-6s Value = %s' % (key, value))


# Swapping using simultaneous assignment
j = 5
k = 12

# print("j = %-4s k = %s" % (j, k))
#
# j, k = k, j
# print("j = %-4s k = %s" % (j, k))


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


fibonacci_iter = fibonacci()
num = next(fibonacci_iter)

while num < 100:
    print(num)
    num = next(fibonacci_iter)
