from typing import List


class Library:
    def __init__(self, name: str, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.name = name
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library: {self.name}\nCity: {self.city}\nStreet: {self.street}\nZip code: {self.zip_code}\n' \
               f'Open hours: {self.open_hours}\nPhone: {self.phone}\n'


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Employee:\nFirst name: {self.first_name}\nLast name: {self.last_name}\n' \
               f'Hire date: {self.hire_date}\nBirth date: {self.birth_date}\n' \
               f'Address: {self.city}, {self.street}, {self.zip_code}\nPhone: {self.phone}\n'


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Book:\nAuthor: {self.author_name} {self.author_surname}\n' \
               f'Published on: {self.publication_date}\nNumber of pages: {self.number_of_pages}\n' \
               f'Location:\n{str(self.library)}'


class Order:
    def __init__(self, employee: Employee, student: str, books: List[Book], order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_str = '\n'.join([str(book) for book in self.books])
        return f'Order details:\n{str(self.employee)}\nStudent: {self.student}\n' \
               f'Books ordered:\n{book_str}\nOrder date: {self.order_date}'


library_CNTI = Library('CNTI', 'Katowice', 'Bogucicka 5', '40-227', '8:00-18:00', '32 257 73 48')
library_CNIBA = Library('CNIBA', 'Katowice', 'Bankowa 11a', '40-007', '8:00-20:00', '32 786 51 30')

book1 = Book(library_CNTI, "2022-01-01", "John", "Doe", 200)
book2 = Book(library_CNTI, "2022-02-01", "Jane", "Smith", 250)
book3 = Book(library_CNIBA, "2022-03-01", "Bob", "Johnson", 180)
book4 = Book(library_CNIBA, "2022-04-01", "Alice", "Brown", 220)
book5 = Book(library_CNTI, "2022-05-01", "Charlie", "Williams", 300)

employee1 = Employee("John", "Doe", "2022-01-01", "1990-05-15", "City1", "Street1", "12345", '123456789')
employee3 = Employee("Bob", "Johnson", "2022-03-01", "1995-03-10", "City3", "Street3", "54321", '111222333')

order_01 = Order(employee1, 'Maciek Kozbial', books=[book1, book2], order_date='2023-11-13')
order_02 = Order(employee3, 'Pawel Kalmuk', books=[book4, book5], order_date='2023-11-11')

print(order_01)
print(order_02)
