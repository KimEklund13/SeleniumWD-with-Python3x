"""
Exceptions are errors
We should handle errors in our code
to make sure the code is working the way we want and is handling all the unwanted issues
Link to 3.8 built-in exceptions: https://docs.python.org/3/library/exceptions.html
"""

def exception_handling():
    try:
        a = 10
        b = "some string"
        c = 0

        d = (a + b) / c
        print(d)
    # except ZeroDivisionError:
    #     print("ZeroDivisionError Here")
    #     # This will print in the console instead of the console giving you an error
    # except TypeError:
    #     print("Can't add string to integer")
    except:
        print("Got the exception")

exception_handling()