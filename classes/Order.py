from typing import List
from classes.Employee import Employee
from classes.Book import Book


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
