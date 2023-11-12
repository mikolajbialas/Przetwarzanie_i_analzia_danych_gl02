from typing import List


def func(first_list: List[int], sec_list: List[int]) -> List[int]:
    connected_list = first_list + sec_list
    without_duplicate_list = []
    power_3_list = []

    for num in connected_list:
        if num not in without_duplicate_list:
            without_duplicate_list.append(num)

    for num in without_duplicate_list:
        power_3_list.append(num ** 3)

    return power_3_list


print(func([2, 3, 4, 5], [1, 2, 4, 5]))
