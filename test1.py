from random import random, randint
import datetime
import math

# class Student:
#     def __init__(self, student_number, student_name, student_class):
#         self.student_number = student_number
#         self.student_name = student_name
#         self.student_class = student_class
#
#
# students = []
#
# file = open("test3.txt", "a")
# for i in range(1):
#     student_number = int(input("Enter student number : "))
#     student_name = input("Enter student name : ")
#     student_class = input("Enter student class : ")
#     file.write("\n"+str(student_number)+" "+student_name+" "+student_class)
#
# file.close()
#
# file = open("test3.txt", "r")
# for count, line in enumerate(file):
#     data = str(line).split(" ")
#     s = Student(data[0], data[1], data[2])
#     students.append(s)
#
# file.close()
# for i in students:
#     print(i.student_number, i.student_name, i.student_class)

# print(int(random() * 10))
# print(randint(1, 11))
# x = datetime.now().strftime("%A")
# print(x)

my_dict = {
    "name": "Heba",
    "age": 19,
    "uni": "Alazhar",
    "car": "Ford"
}

for key, value in my_dict.items():
    print(key, value)

