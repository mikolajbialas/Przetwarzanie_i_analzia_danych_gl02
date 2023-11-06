def multiply_by_two(list_of_numbers):
    final_list = []
    for number in list_of_numbers:
        number = number * 2
        final_list.append(number)
    return final_list


list_of_num = [2, 5, 6, 7, 8]

print(multiply_by_two(list_of_num))
