cars = ["bmw", "honda", "audi"]

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1, "jeep")
print(cars)

x = cars.index("honda")  # trying to find this element in the list
print(x)  #prints 2. If there were two hondas, it will give 2 as the first honda in the list.

y = cars.pop()  # removes the item from the list. By default, it will remove from the end (like append by default appends to end)
print(y)
print(cars)  # this will print with Benz removed

cars.remove("jeep")  # removes a particular element
print(cars)

slicing = cars[0:2]  # 0 is inclusive, 2 is not inclusive. Will return bmw and honda.
print(slicing)

print(cars)
cars.sort()
print(cars)  # gives you the list in alphabetical order