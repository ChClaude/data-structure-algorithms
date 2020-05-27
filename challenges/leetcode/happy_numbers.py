
def happy_numbers(num: int):
    """
    leetcode.com #202
    A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
    Return True if n is a happy number, and False if not.
    :param num: positive
    :return: true if num is a happy number, false otherwise.
    """

    str_num = str(num)
    num_list = list(str_num)
    running = True

    while running:
        mysum = 0
        for digit in num_list:
            mysum = (int(digit)) ** 2
        if mysum == 1:
            return True
        str_num = str(mysum)
        num_list = list(str_num)


print(happy_numbers(19))
