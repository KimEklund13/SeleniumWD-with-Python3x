"""
Some built-in functions:
max(): It takes any number of arguments and returns the largest one

min(): It takes any number of arguments and returns the smallest one

abs(): It returns the absolute value of the number, that number's distance from 0.
It always returns a positive value and it only takes a single number.

type(): It returns the type of the data it receives as an argument
"""

def largest_num(*args):  # * means it can accept any number of arguments. Only necessary in method signature.
    print(max(args))
    return(max(args))

x = largest_num(-20, -10, 0, 10, 100)  # Prints 100

def smallest_num(*args):
    print(min(args))

smallest_num(-20, -10, 0, 10, 100)  # Prints -20


def abs_function(a):
    print(abs(a))

abs_function(-20)  # Prints 20 (always positive)
abs_function(20)  # Prints 20

print("**"*20)

print(type(99))  # Prints 'int'
print(type(99.9))  # Prints 'float'
print(type("99.9"))  # Prints 'str'
