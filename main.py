from classes.Student import Student
from classes.Library import Library
from classes.Book import Book
from classes.Employee import Employee
from classes.Order import Order
from classes.House import House
from classes.Flat import Flat

student_01 = Student("Maciek", [80, 100, 70])
student_02 = Student("Kamil", [20, 30, 15])

print("Exercise 1")
print(student_01.is_passed())
print(student_02.is_passed())
print("-" * 30)

library_CNTI = Library(
    "CNTI", "Katowice", "Bogucicka 5", "40-227", "8:00-18:00", "32 257 73 48"
)
library_CNIBA = Library(
    "CNIBA", "Katowice", "Bankowa 11a", "40-007", "8:00-20:00", "32 786 51 30"
)

book1 = Book(library_CNTI, "2022-01-01", "John", "Doe", 200)
book2 = Book(library_CNTI, "2022-02-01", "Jane", "Smith", 250)
book3 = Book(library_CNIBA, "2022-03-01", "Bob", "Johnson", 180)
book4 = Book(library_CNIBA, "2022-04-01", "Alice", "Brown", 220)
book5 = Book(library_CNTI, "2022-05-01", "Charlie", "Williams", 300)

employee1 = Employee(
    "John",
    "Doe",
    "2022-01-01",
    "1990-05-15",
    "City1",
    "Street1",
    "12345",
    "123456789",
)
employee3 = Employee(
    "Bob",
    "Johnson",
    "2022-03-01",
    "1995-03-10",
    "City3",
    "Street3",
    "54321",
    "111222333",
)

order_01 = Order(
    employee1, "Maciek Kozbial", books=[book1, book2], order_date="2023-11-13"
)
order_02 = Order(
    employee3, "Pawel Kalmuk", books=[book4, book5], order_date="2023-11-11"
)

print("Exercise 2\n")
print(order_01)
print(order_02)
print("-" * 30 + "\n")

house1 = House(
    area=150, rooms=4, price=300000, address="ul. Bogucika 1", plot=500
)
flat1 = Flat(
    area=80, rooms=2, price=150000, address="ul. Jana Matejki 2", floor=2
)

print("Exercise 3\n")
print(house1)
print(flat1)
