def pascals_triangle(row):
    """
    leetcode.com - Question 119
    :param row: number representing a given row in the pascal's triangle
    :return:
    """
    triangle = []
    column = 0

    for x in range(0, row):
        column = column + 1
        for y in range(0, column):
            print(y)


print(pascals_triangle(2))


# Elvis' Codes
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        # Algorithm:
        #     Have a list that takes lists(pascal numbers in that row)
        #     of each indexand return the last added list when the
        #     index is reached.

        if rowIndex == 0:
            return [1]
        elif rowIndex < 0:
            return []

        lists = []

        loops = rowIndex + 1
        for i in range(loops):
            if i == 0:
                lists.append([1]);
            elif i == 1:
                lists.append([1, 1])

            else:
                row_list = [1]
                for j in range(len(lists[i - 1]) - 1):
                    row_list.append(lists[i - 1][j] + lists[i - 1][j + 1])
                row_list.append(1)

                lists.append(row_list)

        return lists[rowIndex]
