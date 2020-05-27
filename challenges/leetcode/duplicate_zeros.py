def duplicate_zeros(arr: list):
    length = len(arr)

    index = length
    for x in range(length):
        if x == index:
            index = length
            continue

        if arr[x] == 0:
            arr.insert(x, 0)
            index = x + 1
            arr.pop()
            x = x + 1


my_num_arr = [1, 0, 2, 3, 0, 4, 5, 0]
my_num_arr_2 = [1, 2, 3]


# duplicate_zeros(my_num_arr)
# duplicate_zeros(my_num_arr_2)
# print(my_num_arr)  # [1,0,0,2,3,0,0,4]
# print(my_num_arr_2)  # [1,2,3]


def find_all_numbers_m(nums: list):
    length = len(nums)
    if length > 1:
        missing_nums = []
        minim = min(nums)
        maxim = max(nums)

        if maxim == minim:
            missing_nums = list(range(1, minim))
            for x in range(minim, length + 1):
                if x not in nums:
                    missing_nums.append(x)
            return missing_nums
        else:
            missing_nums = list(range(1, minim))
            for x in range(minim, length + 1):
                if x in nums:
                    continue
                missing_nums.append(x)
            return missing_nums

    return []


my_nums = [4, 3, 2, 7, 8, 2, 3, 1]

print(find_all_numbers_m(my_nums))  # [5,6]


# From Elvis
# 448. Find All Numbers Disappeared in an Array
def find_all_numbers(nums):
    if len(nums) == 0: return []

    returned_list = set()  # Set because I don't want to have duplicates
    arr_length = len(nums)

    for i in range(1, arr_length + 1):
        if i not in nums:
            returned_list.add(i)

    return returned_list
