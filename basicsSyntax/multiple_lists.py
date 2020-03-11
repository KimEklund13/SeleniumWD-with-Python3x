"""
Iterating over multiple lists
"""

l1 = [1, 2, 3]
l2 = [6, 7, 8, 20, 30, 40]

for a, b in zip(l1, l2):
    print(a)  # printing item from first list
    print(b)  # printing item from second list
    # This will run as many times as the length of the shortest list (3 times)