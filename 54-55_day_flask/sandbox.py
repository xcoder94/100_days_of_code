# Function inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# First-class objects, can be passed around as arguments e.g.
# in/string/float etc.
# def calculate(calc_func, n1, n2):
#     return calc_func(n1, n2)
#
#
# result = calculate(multiply, 2, 3)
# print(result)


# Nested Functions
# def outer_function():
#     print('I am outer')
#
#     def nested_function():
#         print('I am inner')
#
#     nested_function()
#
#
# outer_function()


# Functions can be returned from other functions
# def outer_function():
#     print('I am outer')
#
#     def nested_function():
#         print('I am inner')
#
#     return nested_function
#
#
# inner_function = outer_function()
# inner_function()


# Python Decorator Functions
# import time
#
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         # Do something before
#         function()
#         function()
#         # Do something after
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print('Hello')
#
#
# @delay_decorator
# def say_hello():
#     print('Bye')
#
#
# def say_greeting():
#     print('How are you')
#
#
# # say_hello()
# decorated_function = delay_decorator(say_greeting)
# decorated_function()

# Coding challenge
# import time
#
# current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970
#
#
# # Write your code below 👇
#
# def speed_calc_decorator(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(start_time)
#         print(end_time)
#         print(f'{func.__name__} ran in {end_time - start_time} seconds')
#
#     return wrapper
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         a = i * i
#         # print(a)
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         b = i * i
#         print(b)
#
#
# fast_function()
# slow_function()

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
#
# def is_auth_decorator(func):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             func(args[0])
#     return wrapper


# @is_auth_decorator
# def create_blog_post(user):
#     print(f'This is {user.name} \'s new blog post.')
#
#
# new_user = User('Rustam')
# new_user.is_logged_in = True
# create_blog_post(new_user)

# Coding Challenge
inputs = eval(input())


# TODO: Create the logging_decorator() function 👇


def logging_decorator(fn):
    def wrapper(*args):
        print(f'You called {fn.__name__}{args}')
        result = fn(args[0], args[1], args[2])
        print(f'It returned {result}')

    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
