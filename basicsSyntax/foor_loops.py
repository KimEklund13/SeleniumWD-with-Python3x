"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""

my_string = "abcabc"

for c in my_string:
    if c == "a":
        print("A", end=" ")  # This will put all the print out on a single line on the console
    else:
        print(c, end=" ")

print()

cars = ["bmw", "benz", "honda"]

for car in cars:
    print(car)

nums = [1, 2, 3]

for n in nums:
    print(n * 10)


d = {"one": 1, "two": 2, "three": 3}
for key in d:
    print(key + " " + str(d[key]))

print("*"*20)

for k,v in d.items():  # retrieves both the keys and values in the dictionary by using .items
    print(k)
    print(v)