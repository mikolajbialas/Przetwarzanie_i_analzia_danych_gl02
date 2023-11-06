def print_even(list_of_numbers):
    for number in list_of_numbers:
        if number % 2 == 0:
            print(number)


list_of_num = [i for i in range(1,11)]
print_even(list_of_num)
