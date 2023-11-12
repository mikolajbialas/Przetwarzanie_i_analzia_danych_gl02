def return_full_name(name: str, surname: str) -> str:
    final_str = f'Czesc {name} {surname}!'
    return final_str


string = return_full_name('Mikolaj', 'Bialas')
print(string)
