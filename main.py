from python_basic.zad_1 import print_names
from python_basic.zad_2 import multiply_by_two
from python_basic.zad_3 import print_even
from python_basic.zad_4 import print_every_other_element

print('Exercise 1')
names = ['Asia', 'Kasia', 'Tomek', 'Marcin', 'Piotrek']
print_names(names)
print('-' * 30)

print('Exercise 2')
list_of_num = [2, 5, 6, 7, 8]
print(multiply_by_two(list_of_num))
print('-' * 30)

print('Exercise 3')
list_of_num = [i for i in range(1, 11)]
print_even(list_of_num)
print('-' * 30)

print('Exercise 4')
list_of_num = [i for i in range(1, 20)]
print_every_other_element(list_of_num)
