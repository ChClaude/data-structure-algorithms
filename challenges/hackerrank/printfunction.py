def print_f(num):
    num = int(num)
    y = ''.join([str(x + 1) for x in range(num)])


def find_sum(limit=1000):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    :return: sum of multiples of 3 and 5 below limit (default = 1000)
    """
    mysum = 0
    for x in range(limit):
        if x % 3 == 0 or x % 5 == 0: mysum += x

    return mysum


print(find_sum())
