"""
Classes: templates that define the object
"""

class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of car: " + self.make)
        print("Model of car: " + self.model)

# Create instance outside of the class

print(Car.wheels)

c1 = Car("bmw", "550i")
c1.info()
c1.wheels = 3
print(c1.wheels)

c2 = Car("benz", "E350")
c2.info()
print(c2.wheels)