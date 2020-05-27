def isomorphic_string(s: str, t: str):
    """
    https://leetcode.com/problems/isomorphic-strings/
    Given two strings s and t, determine if they are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t. 7
    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

    :param s:
    :param t:
    :return:
    """

    # Example # 1:
    #
    # Input: s = "egg", t = "add"
    # Output: true
    # Example # 2:
    #
    # Input: s = "foo", t = "bar"
    # Output: false
    # Example # 3:
    #
    # Input: s = "paper", t = "title"
    # Output: true

    length = len(t)
    my_list = []
    if len(s) == length:
        s_list = list(s)
        t_list = list(t)

        for x in range(length):
            my_tuple = (s_list[x], t_list[x])
            my_list.append(my_tuple)

    my_dict = dict(my_list)

    spot_duplicate = []
    for k, v in my_dict.items():
        if v in spot_duplicate:
            return False
        else:
            spot_duplicate.append(v)

    return True


print(isomorphic_string('title', 'paper'))
