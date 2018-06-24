"""
Following are the topics we will cover today.

1) Creating and Calling Function
2) Unnamed and named Parameters
3) Anonymous Lambda Function
4) Iterator
5) Generator
6) Generator vs Iterator

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

# _add_func = lambda ele_1, ele_2: ele_1 + ele_2
#
# _add_func(34, 45)
#
# _power = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))


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
#
# print(data.next())
# print(data.next())
# print(data.next())
# print(data.next())

# #############################################################################
# 5) Generator
# #############################################################################


# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# for item in simple_generator():
#     print(item)


# def fib(limit):
#     # Initialize first two Fibonacci Numbers
#     a, b = 0, 1
#
#     # One by one yield next Fibonacci Number
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
# for i in fib(5):
#     print(i)


