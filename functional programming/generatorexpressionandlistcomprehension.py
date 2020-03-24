line_list = [' line 1\n', 'line 2 \n', ' line 3\n', 'line 4 \n', ' line 5\n', 'line 6 \n', ' line 7\n', 'line 8 \n']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)
# print(stripped_iter.__next__())

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
# print(stripped_list)

# You can select only certain elements by adding an "if" condition
stripped_list2 = [line.strip() for line in line_list
                  if line != ""]
# print(stripped_list2)


num_list = [1, 2, 4, 5, 9, 10, 6, 15, 17, 22]
num_doublelist = [num*2 for num in num_list if num % 3 == 0]
# print(num_doublelist)
print(sum(num for num in num_list))

seq1 = "abc"
seq2 = (1, 2, 3)

seq3 = [(x, y) for x in seq1 for y in seq2]
# print(seq3[0])
