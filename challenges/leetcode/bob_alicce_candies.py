import functools
import itertools
import operator


# Bob and ALice candies challenge


def share_candy(b_candies, a_candies):
    """
    Bob and Alice candies share method
    :param b_candies: list of integer numbers representing bob's candies
    :param a_candies: list of integer numbers representing alice's candies
    :return: tuple representing the values that must be returned from the two arrays so as to have an
                equal sum of element in both arrays
    """
    for x in b_candies:
        for y in a_candies:
            b_candies_new = list(b_candies)
            a_candies_new = list(a_candies)

            b_candies_new.remove(x)
            a_candies_new.remove(y)

            if sum(b_candies) == sum(a_candies): return (x, y)


# share_candy([1, 1], [2, 2])


def bob_ans(A, B):
    a_len = len(A)
    b_len = len(B)
    ans = list()
    solved = False
    sa = sum(A)
    sb = sum(B)

    for i in range(a_len):
        if not solved:
            for j in range(b_len):
                if sa - A[i] + B[j] == sb - B[j] + A[i]:
                    ans.append(A[i])
                    ans.append(B[j])
                    solved = True
                    break
        else:
            break
    return ans


print(bob_ans([1, 1], [2, 2]))
