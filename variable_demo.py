"""
This is a variable demo
"""


class MyClass(object):
    """
    This is my class
    """

    def __init__(self):
        """
        This is init method to initialize method parameter
        """


def function_function():
    """
    This is a function
    :return:
    """

#
# my_list = ['Parth', 'Shiv', 'Sandeep', 'Ritika']
#
# my_list.append('Srikant')
# # my_list.remove('Shiv')
#
# for index, item in enumerate(my_list):
#     print(index, item)

my_dictionary = {
    'key': 'value',
    'key2': ['value', 'value2'],
    'key3': {'nested_key': 'nested_value'},
}
print(my_dictionary['key2'])
print(my_dictionary.get('key5', 'key does not found in dictionary'))

for key, value in my_dictionary.items():
    print(key, value)

print(my_dictionary.keys())
print(my_dictionary.values())


"""
USER_DATA = {
    "Parth": {"phone_no": 1234456678, "address": "home"},
    "Shiv": {"phone_no": 2345456464, "address": "home____"},
    "Gaurav": {"phone_no": 32422324423, "address": "home"},
    "Ganesh": {"phone_no": 21313121213, "address": "home"},
    "Parth": "Parth",
}

USER_DATA.get('Shiva')['relation'] = 'test'


print(USER_DATA.get("Shiv").get("address"))
"""
# for key, value in user_data.items():
#     print(key, type(key), type(value), value)
"""
| Name                          | Phone No   | Address      | Relationship  |
| Parth Patel                   | 0987654321 | Home         | me            |
| Partth PPPPPPPtel             | 3455435435 | dfdfgdggdfsg | sdfd          |
| sdadfafdsafdsafdasfdsafsadfas |

"""

"""
1 Integer
2 String
3 List
4 Dictionary
5 Set
6 Tuple
7 Object
8 Float
"""

'''

'''