def check_numbers(num_1: int, num_2: int, num_3: int) -> bool:
    if num_1 + num_2 >= num_3:
        return True
    else:
        return False


print(check_numbers(5,2,5))