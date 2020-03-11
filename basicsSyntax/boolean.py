a = True
b = False

print(a)
print(b)

print("********")
print(bool(0))  # Empty values equate to False
print(bool(1))

print("********")
c = ""
print(bool(c))  # Empty strings are False (but an empty string with a space isn't a true empty string.

c = "whatever"
print(bool(c))