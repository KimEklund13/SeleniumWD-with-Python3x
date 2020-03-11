"""
Tuples are like lists but are immutable
They are also defined using parens instead of square brackets
"""

my_list = [1, 2, 3]
print(my_list)

my_list[0] = 0
print(my_list)

my_tuple = (1, 2, 3)
print(my_tuple)

# my_tuple[0] = 0  -- Get an error "tuple object does not support item assignment"
# We can access elements though

print(my_tuple[1:])   # slicing

print(my_tuple.index(2))

print(my_tuple.count(3))  # How many times does "3" appear in the tuple?