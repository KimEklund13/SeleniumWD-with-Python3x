"""
Built-in function
creates a sequence of numbers but does not save them in memory
very useful for generating numbers
"""

print(list(range(0, 10)))  # starting point, ending point (exclusive) -- casted as a list

a = range(0, 10)
print(a)

print(list(a))

steps = range(0, 10, 2)
print(list(steps))  # will print 0, 2, 3, 6, 8 (increments of 2 (steps of 2)

steps3 = range(3, 90, 3)
print(list(steps3))

# l = [1, 2, 3]
for num in range(3):  # Could also use range(1, 4). Can use this range function instead of looping through a list.
    print(num)