"""
Inheritance:
BMW class inherits from the Car class
Child class will inherit from the Parent class
"""

class Car(object):
    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("car started")

    def stop(self):
        print("car stopped")


class BMW(Car):
    def __init__(self):
        # Warning is provided that you have not called the "base" class aka super class
        Car.__init__(self)  # Then we add this, which calls the super init.
        print("You just created the BMW instance")


c = Car()
c.drive()
c.stop()

beemer = BMW()
beemer.stop()
beemer.drive()