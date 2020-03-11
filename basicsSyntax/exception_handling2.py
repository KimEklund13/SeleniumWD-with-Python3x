"""
Exceptions are errors
We should handle errors in our code
to make sure the code is working the way we want and is handling all the unwanted issues
Link to 3.8 built-in exceptions: https://docs.python.org/3/library/exceptions.html
"""

def exception_handling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) / c
        print(d)
    except:
        print("Got the exception")
        raise Exception("This is an exception")
    else:
        print("Because there was no exception, ELSE is executed")
    finally:
        print("This is always executed, no matter what")

exception_handling()