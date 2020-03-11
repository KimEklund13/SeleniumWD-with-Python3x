"""
Exception Handling HW

Create a dictionary "car"
Create 3 keys
make, model, year

Try to access the color key. Remember, we never created the color key,
so its going to throw an exception. You need to handle the exception
using the try, except, and finally block
"""

car = {"make": "bmw", "model": "350i", "year": 2016}

try:
    car["color"]
except:
    print("Key does not exist")
finally:
    print("Search finished")