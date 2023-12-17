from typing import List


class Student:
    def __init__(self, name: str, marks: List):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        avg = 0
        for mark in self.marks:
            avg += mark

        avg = avg / len(self.marks)

        if avg > 50:
            return True
        else:
            return False
