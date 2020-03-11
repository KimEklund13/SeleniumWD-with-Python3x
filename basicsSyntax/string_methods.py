# Accessing characters in a string

first = "nyc"[0]  # To access "n"
city = "sfo"
print(first)

ft = city[0]  # Assigns the first character to ft
print(ft)

"""
len()
lower()
upper()
str()
"""

stri = "This Is a Mixed Case"
print(stri.lower())
print(stri.upper())  # Everything is in CAPS
print(len(stri))  # Length of the string including spaces

print(stri + str(2))  # Type casted the Int 2 and concatenated it to the original string

"""
Concatentation
"""

print("Hello " + " " + " world !!!")

print(first + " " + city)
