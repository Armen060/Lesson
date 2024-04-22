# Ex_7
# with  open('file_1.txt', 'r') as file:
#     ints=[]
#
#     for row in file:
#         for letter in row:
#             if letter.isdigit():
#                 l.append(letter)
# print(l)
# # Ex_6
# import time
#
#
# def decorator(func):
#     def inner(x, y):
#         t1 = time.time()
#         s = func(x, y)
#         t2 = time.time()
#         t = t2 - t1
#         print(t, 'seconds')
#         return s
#
#     return inner

#
# @decorator
# def summa(a, b):
#     return a + b
#
#
# print(summa(10, 2))

# Ex_5
# def authentication(func):
#     def inner():
#         password = input("Enter your password: ")
#         if password == 'qwerty':
#             func()
#         else:
#             print("invalid password")
#     return inner
# @authentication
# def welcome():
#     print("HI, Welcome my friend ")
# welcome()
# Ex_2
import math


# def decorator(func):
#     def inner(x, y):
#         return math.log(math.log(1024, 2) - math.log(64, 2), 2)
#
#     return inner
#
#
# @decorator
# def log(a, b):
#     return (a - b)
#
#
# print(log(1024, 64))
# Ex_1
# def decorator_1(func):
#     def inner(x, y):
#         return f"'\033[42m'{x-y}'"
#
#
#
#     return inner
#
# def decorator_2(func):
#     def inner (x,y):
#         return f"'\033[101m'{x-y}'"
#     return inner
#
# def decorator_3(func):
#     def inner (x,y):
#         return f"'\033[104m'{x-y}'"
#     return inner
#
# @decorator_1
# @decorator_2
# @decorator_3
#
# def summa(a, b):
#     return (a + b)
#
#
# print(summa(1, 2))

