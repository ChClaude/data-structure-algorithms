import unittest


def reverse_sequence(char_arr): # ['n', 'a', 'a', 'c', 'p']
    length = len(char_arr)
    for x in range(length):
        char_arr.append(char_arr[length - x - 1])

    for x in range(length):
        char_arr.remove(char_arr[x])


# mylist = ['t', 'e', 's', 'p']
# print(mylist)
# reverse_sequence(mylist)
# print(mylist)

# Elvis's code
def reverse(chars):
    loop_length = int(len(chars) / 2)
    left, right = 0, len(chars) - 1

    for i in range(0, loop_length):
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp

        left += 1
        right -= 1

# test
class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse_sequence(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse_sequence(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse_sequence(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)
