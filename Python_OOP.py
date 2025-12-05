class Class:

    def __init__(self, students):
        self.students = students

class Person:

    def __init__(self, details):
        self.details = details

class School:

    def __init__(self, address, postCodesAccepted, students):
        self.address = address
        self.postCodesAccepted = postCodesAccepted
        self.students = students


class Employee(Person):

    def __init__(self, salary):
        super().__init__()
        self.salary = salary

class Student(Person):

    def __init__(self, grade):
        super().__init__()
        self.grade = grade

class Teacher(Employee):

    def __init__(self, teaches):
        super().__init__()
        self.teaches = teaches


Transfiguration = Class()
