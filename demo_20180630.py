"""
Following are the topics we will cover today.

1) Project discussion
2) Decorator

Assignments :
1) Create 10 decorators

2) write a decorator function and 3-4 functions to check user have that
   permission or not.

   Create list of permissions (at least 15 permissions)
   permissions = ['can_create_user', 'can_delete_user', ....]
   Create dictionary of user  (at least 4 users)
   users = {
        '<email_id/phone_no/user_id>' : {
            'roles': [role_id1],
            'permissions': ['can_read_user']
        }
   }
   Create dictionary of roles (at least 5 roles)
   roles = {
        'id': 1,
        'permissions': ['can_create_user', 'can_delete_user']
   }

   Functions
   def create_user(user_id, 'can_create_user')
   def delete_user(user_id, 'can_delete_user')
   .
   .
   .

"""

# #############################################################################
# 1) Project discussion
# #############################################################################

# Ganesh's Project
"""
Definition : AWS utility in python which will manage aws services
"""

# Ritika's Project
"""
Definition : Education Institute's Assignment Management System 
"""


# #############################################################################
# 2) Decorator
# #############################################################################

# Closer Function
# Nested Function

#
# def decorator_function(name):
#     print("hello from decorators")
#
#     def greetings():
#         return F"hello {name} from greetings"
#
#     return greetings
#
#
# def display(name):
#     print(name)
#
#
# display = decorator_function(display)
# display()

#
# def p_tag_decorator(_function):
#     def wrapper(name):
#         print('We are in Wrapper function')
#         _format = F"<p>{name}</p>"
#         _function(_format)
#
#     return wrapper
#
#
# def b_tag_decorator(_function):
#     def wrapper(name):
#         print('We are in b Wrapper function')
#         _format = F"<b>{name}</b>"
#         _function(_format)
#
#     return wrapper
#
#
# @b_tag_decorator
# @p_tag_decorator




# @p_tag_decorator
def display_2(string_data):
    print(string_data)


# display("Parth")
# display_2("Hi Parth, what happening with your life..")



def u_tag_decorator(display_function):

    def wrapper_function(name):
        print('This is wrapper function of u tag decorator')
        updated_string = F"<u>{name}</u>"
        display_function(updated_string)

    return wrapper_function
#
# test = u_tag_decorator(display)
#
# test("parth")

@u_tag_decorator
def display(name):
    print(name)

display('This is my 1st decorator')