"""
Built-in modules have methods we can import and use
Examples are `math`, `numbers`
You use `import math` and call methods by `math.function_name()`
but that pulls in ALL the methods and takes up a lot of space.
You can just import the functions you need by using
`from math import sqrt` and you won't need the math.sqrt - you can just use `sqrt`
"""

import math
# import basicsSyntax.modules2 as car  # importing our custom module
# from basicsSyntax import modules2
from basicsSyntax.modules2 import info
# from math import sqrt

class Modules():

    def builtin_modules(self):
        print(math.sqrt(100))
        # print(sqrt(100))

    def car_description(self):
        make = "bmw"
        model = "550i"
        # car.info(make, model)
        # modules2.info(make, model)
        info(make, model)

m = Modules()
m.builtin_modules()

m.car_description()
