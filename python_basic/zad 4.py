def print_every_other_element(list_of_numbers):
    for i in range(len(list_of_numbers)):
        if i % 2 != 0:
            print(list_of_numbers[i])


list_of_num = [i for i in range(1, 20)]
print_every_other_element(list_of_num)
