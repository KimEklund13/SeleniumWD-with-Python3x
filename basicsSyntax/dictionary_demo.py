"""
Dictionaries are not sequenced like lists.
They are stored in key-value pairs.
Dictionary items are in curly brackets{ } separated with commas {'k1':'v1', 'k2':'v2'}
"""

car = {"make": "bmw", "model": "550i", "year": 2016}
print(car)

# print(car[0[) will not work. You cannot access elements like a list.

print(car["model"])  # Will print the value (550i)

empty_d = {}
print(empty_d)

empty_d["one"] = 1  # Adding elements to dictionary. Adding a [key] and assigning a value
print(empty_d)

empty_d["two"] = 2
print(empty_d)


sum_of_value = empty_d["two"] + 8  # gets value of key, adds 8 to it
print(sum_of_value)