"""
Create a class "FRUIT"

1. Define 3 methods in this class
__init__()
nutrition()
fruit_shape()

Print anything you like in these methods

2. Create one more class (Any fruit name)
This class should inherit from the Fruit class.

Define 3 methods:
__init__()
nutrition()
color()

Print anything you like in these methods

3. Create instances of these classes and call methods from them.
Call methods from the base class also using the instance of the child class
"""

class Fruit(object):

    def __init__(self):
        print("Base fruit initialized")

    def nutrition(self):
        print("Base fruit nutrition facts: xyz")

    def fruit_shape(self):
        print("Base fruit's fruit shape is so basic")


class Banana(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("Banana initialized")

    def nutrition(self):
        print("Bananas are full of potassium")

    def color(self):
        print("Bananas are yellow")


pear = Fruit()
pear.nutrition()
pear.fruit_shape()

banana = Banana()
banana.nutrition()
banana.color()
banana.fruit_shape()

