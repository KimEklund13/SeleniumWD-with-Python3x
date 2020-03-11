"""
break: to break out of the CLOSEST enclosing loop
continue: go to the start of the closest enclosing loop

The "else" will always execute in a while loop unless it follows a break statement
"""


x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

    # if x == 8:
    #     break  # once the value of x becomes 8, then the "break" triggers and the loop stops.
    print("This example is awesome")
    print("*"*20)
else:
    print("Done with the loop")

# x = 0
# while x < 10:
#     print("Value of x is: " + str(x))
#     x = x + 1
#
#     if x == 8:
#         continue  # When the code encounters this, it will go back to the beginning of the loop, but not do anything after this
#     print("This example is awesome")
#     print("*"*20)
#
# print("Done with the loop")