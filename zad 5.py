from typing import List


def s_func(list_of_num: List[int], number: int) -> bool:
    if number in list_of_num:
        return True
    else:
        return False


l = [213, 123, 213, 2]
num = 6

print(s_func(l, num))
