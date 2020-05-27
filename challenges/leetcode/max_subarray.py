from challenges.leetcode.happy_numbers import happy_numbers


def max_subarray(arr: list):
    """
    Leetcode.com #53
    Given an integer array nums, find the contiguous subarray
    (containing at least one number) which has the largest sum and return its sum.
    """
    print(arr)


def arranging_coins(num: int):
    """
    leetcode.com #441
    You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
    Given n, find the total number of full staircase rows that can be formed.

    n is a non-negative integer and fits within the range of a 32-bit signed integer.
    :return:
    """
    rows = []
    for x in range(1, num):
        num -= x
        if len(rows) == num:
            return len(rows)
        elif len(rows) + 1 > num:
            return len(rows)
        rows.append(x)


# print(arranging_coins(10))

print(happy_numbers(215))


# From Elvis
def arrange_coins_e(self, n: int) -> int:
    # Algorithm:
    # Remove the number of coins that has to be used
    # for each row from n until its either zero or negative.

    if not n: return 0

    i = 1
    complete_stairs = 0

    while n > 0:
        n -= i

        if n >= 0:
            complete_stairs += 1

        i += 1

    return complete_stairs
