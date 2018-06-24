"""
Following are the topics we will cover today.

# 1) Creating and Calling Function
# 2) Unnamed and named Parameters
3) Anonymous Lambda Function
4) Iterator
5) Generator
6) Generator vs Iterator
7) Recursive Function

"""

# #############################################################################
# 1) Creating and Calling Function
# #############################################################################


# def greetings(person="Parth"):
#     """
#     This is a greeting function
#     :param person: person name
#     """
#     greeting_message = F"Hello {person}."
#     return greeting_message


# #############################################################################
# 2) Unnamed and Named Parameters
# #############################################################################

# numbers = [1, 2, 5, 73, 34, 43, 4, 34, 55, 0.4]
#
#
# def _addition(*args, **kwargs):
#     """
#     addition of passed arguments
#     :param args:
#     :param kwargs
#     :return: sum of arguments
#     """
#     total = sum(args)
#     greeting = [
#         greetings(value) for value in kwargs.values()
#     ]
#     return total, greeting


# total, greet = _addition(*numbers, **{'Dept': 'Parth', 'Xyz': 'Ganesh'})
# print(total, greet)

# #############################################################################
# 3) Anonymous Lambda Function
# #############################################################################

"""
Lambda 

lambda object : operation/expression 
map(lambda object : operation/expression, iterable object) 
"""


# _add_func = lambda ele_1, ele_2: ele_1 + ele_2
#
# _add_func(34, 45)
#
# _sq = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))


# #############################################################################
# 4) Iterator
# #############################################################################

#
# class MyRange:
#     """
#     my range function
#     """
#     def __init__(self, n):
#         self.i = 0
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.i < self.n:
#             i = self.i
#             self.i += 1
#             return i
#         else:
#             raise StopIteration()
#
# data = MyRange(5)

# print(data.next())
# print(data.next())
# print(data.next())
# print(data.next())

# #############################################################################
# 5) Generator
# #############################################################################

#
# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# for item in simple_generator():
#     print(item)


def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
        print("----", a, b)


#
#
# for i in fib(5):
#     print(i)


# def factorial(number):
#     output = 1
#     for i in range(1, number+1):
#         output *= i
#
#     return output
#
#
# print(factorial(5))


def factorial(number):
    output = 1
    fact_no = 1

    while fact_no <= number:
        output *= fact_no
        yield output
        fact_no += 1


# for i in factorial(5):
#     print(i)

from random import random


def fiz_buzz(number):
    iteration_no = 1

    while iteration_no <= number:
        no = int(random() * 100)
        op = no
        if no % 15 == 0:
            op = 'FizBuz'

        elif no % 5 == 0:
            op = 'Buz'

        elif no % 3 == 0:
            op = 'Fiz'

        yield op
        iteration_no += 1


# for i in fiz_buzz(10):
#     print(i)

def check_fiz_buz(no):
    op = no
    if no % 15 == 0:
        op = 'FizBuz'

    elif no % 5 == 0:
        op = 'Buz'

    elif no % 3 == 0:
        op = 'Fiz'

    return op


def fiz_buz_2(number):
    for i in range(0, number):
        no = int(random() * 100)
        yield check_fiz_buz(no)


# for i in fiz_buz_2(10):
#     print(i)

# #############################################################################
# 7) Recursive Function
# #############################################################################

def prime(limit):
    for no in range(1, limit + 1):
        flag = True
        for divider in range(2, no):
            if no % divider == 0:
                flag = False
                break
        if flag:
            print(F"{no} is Prime.")


def prime_re(start, limit):

    if start == limit:
        return

    flag = True
    for divider in range(2, start):
        if start % divider == 0:
            flag = False
            break
    if flag:
        print(F"{start} is Prime.")

    prime_re(start+1, limit)

#
# prime_re(1, 14)