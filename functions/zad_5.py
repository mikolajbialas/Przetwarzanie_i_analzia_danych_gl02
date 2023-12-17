from typing import List


def check_if_in_list(list_of_num: List[int], number: int) -> bool:
    if number in list_of_num:
        return True
    else:
        return False
