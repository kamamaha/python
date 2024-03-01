# Zadanie 1 #######################################################################

# nums = [4, 6, 8, 24, 12, 2]
# def max_index():
#    a = [index for index, value in enumerate(nums) if value == max(nums)]
#    print(a)
# max_index()

# Zadanie 3 #######################################################################

# def fizz_buzz(a):
#     if a % 3 == 0:
#         print("Frizz")
#     elif a % 5 == 0:
#         print("Buzz")
#     elif a % 3 == 0 and a % 5 == 0:
#         print("FrizzBuzz")
#     else:
#         print(a)
# fizz_buzz(13)

# Zadanie 4 #######################################################################

# def multiply(*args):
#     number = 1
#     for a in args:
#         number *= a
#     return number
# print(multiply(2, 10, 10))

# Zadanie 5 #######################################################################
# NIE WIEM
# Zadanie 6 #######################################################################

# def select_list(list):
#     for i in list:
#         if i >= 10:
#             print(i)
# a = [1,2,4,5,6,7,8,9,11,12]
# select_list(a)

# KLASY ...........................................................................
# Zadanie 1 #######################################################################

# class Student():
#     """informations about student"""
#     def __init__(self, name, lastname, age, degree):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.degree = degree
#     def print_info(self):
#         print("Student nazywa się " + self.name.title() + " " + self.lastname.title() + " ma lat " + str(self.age) + " i studiuje " + self.degree.title())
#
# student = Student("Paweł", "Nowak", 13, "informatyka")
# student.print_info()

