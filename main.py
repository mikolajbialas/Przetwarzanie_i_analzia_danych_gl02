from functions.zad_1 import return_full_name
from functions.zad_2 import multipy
from functions.zad_3 import is_even
from functions.zad_4 import check_numbers
from functions.zad_5 import check_if_in_list
from functions.zad_6 import rm_duplicates_and_raise_to_power_3

print('Exercise 1')
string = return_full_name('Mikolaj', 'Bialas')
print(string)
print('-' * 30)

print('Exercise 2')
print(multipy(2, 2))
print('-' * 30)

print('Exercise 3')
entered_number = is_even(5)

if entered_number:
    print("Number is even")
else:
    print('Number is odd')
print('-' * 30)

print('Exercise 4')
print(check_numbers(5, 2, 5))
print('-' * 30)

print('Exercise 5')
list_of_num = [213, 123, 213, 2]
num = 6

print(check_if_in_list(list_of_num, num))
print('-' * 30)

print('Exercise 6')
print(rm_duplicates_and_raise_to_power_3([2, 3, 4, 5], [1, 2, 4, 5]))
print('-' * 30)
