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

    def drive(self):  # there is no override keyword. You can just override like this.
        super().drive()  # (Optional) this calls the method from the base/super class
        print("You are driving a BMW. Enjoy!")

    def headup_display(self):  # method unique to BMW, does not exist in Car class
        print("Headup display engaged on BMW")


c = Car()
c.drive()
c.stop()
# c.headup_display -- this will not work. Super class cannot access child methods

beemer = BMW()
beemer.stop()
beemer.drive()
beemer.headup_display()