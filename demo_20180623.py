"""
1) Builtin Functions: min, max, count, len, split, zip, type, sum, sorted,
replace, slice, isinstance, join
2) Types of function
Function Parameter

Assignment = Create function of Pattern Print Assignment
"""

# #############################################################################
# 1) Builtin Function
# #############################################################################

numbers = [1, 2, 5, 73, 34, 43, 4, 34, 55, 0.4]
# print(min(numbers))
#
# print(max(numbers))
#
# print(numbers.count(34))

_string = "This is what we want. why we here for, we will rock.."

# print(_string.count('we', 25, 50))

# print(len(numbers))
# print(len(_string))


# print(_string.split(' '))
# print(_string[0:1])
# print(_string[::-1])


# numbers_2 = [item for item in range(0, 100)]
# print(numbers_2[0:50:2])
# print(numbers_2[::-1])

# print(_string.replace('we', 'I', 2))
#
x = ['parth', 'ravi', 'srikant', 'ganesh', 'ritika', 'sandeep']
y = [100, 1000, 2000, 30000, 5000, 50000]

my_dictionary = {
    'parth': 100,
    'ravi': '1000',
    'srikant': {
        'classes': 1000,
        'marketing': 1000
    },
    'ganesh': [10000, 5000, '5000', [10000]]
}

# for x_item, y_item in zip(x, y):
#     print(F"{x_item} : {y_item}")

# if isinstance(my_dictionary, list):
#     print("hello this is dictionary")
# else:
#     print("This is not list")
# string_list = ['This is my class', 'That is what i used to do', 'What you suppose to do']
# print(" in addition ".join(string_list))


# multi_line_string = """
# Builtin Functions: min, max, count, len, split, zip, type, sum, sorted,
# replace, slice, isinstance, join
# Builtin Modules: os, sys, re, datetime, glob, math, time, random
# Types of function
# Function Parameter
# """
# from pprint import pprint
# pprint(multi_line_string.splitlines())
# print(sorted(numbers, reverse=True))


# #############################################################################
# # Built in Module
# #############################################################################

import os

print(os.path.abspath(os.curdir))

os.environ['Today'] = "Saturday"

# #############################################################################
# 2) Types of function
# #############################################################################

# ------ Built in Function
# check topic 1

# -----------------------------------------------------------------------------
# ------ User Defined Function

"""
def <function/method name>:
    '''doc string'''
    
    return None
"""


def greetings(person="Parth"):
    """
    This is a greeting function
    :param person: person name
    """
    greeting_message = F"Hello {person}."
    return greeting_message


# greet = greetings('1')
# print(greet)


def _addition(*args, **kwargs):
    """
    addition of passed arguments
    :param args:
    :param kwargs
    :return: sum of arguments
    """
    total = sum(args)
    greeting = [
        greetings(value) for value in kwargs.values()
    ]
    return total, greeting


total, greet = _addition(*numbers, **{'Dept': 'Parth', 'Xyz': 'Ganesh'})
print(total, greet)


# -----------------------------------------------------------------------------
# ------ Closer Function

def greet_me(person):
    """
    addition of passed arguments
    :return: greetings functions
    """
    return greetings(person)

# -----------------------------------------------------------------------------
# ------ Recursive Function


# -----------------------------------------------------------------------------
# ------ Anonymous Function

# -----------------------------------------------------------------------------
# ------ Async Function
