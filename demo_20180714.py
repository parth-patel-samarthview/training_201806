"""
Following are the topics we will cover today.

1)  Basic Exception Handling
2)  Standard Exceptional Hierarchy
3)  Try...Except...Else...Finally clause
4)  Self-Exception class
5) Debugging Errors
6) Debugging with PyCharm

"""

# #############################################################################
# 1)  Basic Exception Handling
# #############################################################################

# Syntext error
# Value Error
# Import Error

dictionary = {
    'name': 'Parth', 'phonne': '098655442445'
}

city = dictionary.get('city', '')

try:
    city = dictionary['city']
except KeyError as error:
    print(error)
    print('city is not present in dictionary')
    pass
finally:
    print("There is no error")

# try:
#     import os as test
# except ImportError:
#     try:
#         import sys as test
#     except ImportError:
#         import math as test
