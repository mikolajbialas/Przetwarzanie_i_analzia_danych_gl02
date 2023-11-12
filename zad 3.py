def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


entered_number = is_even(5)

if entered_number:
    print("Number is even")
else:
    print('Number is odd')
