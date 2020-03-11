# a = 10

# def test_method(a):
#     print("value of local a is: " + str(a))
#     a = 2
#     print("new value of local a is: " + str(a))
#
# print("value of global a is: " + str(a))
#
# test_method(a)
# print("Did the value of global 'a' change? " + str(a))
# Global variables do NOT change inside the method. It remained 10 outside the method.


a = 10

def test_method():
    global a  # tells python to just use the global "a" variable using the global keyword
    print("value of 'a' inside the method is: " + str(a))
    a = 2
    print("new value of 'a' inside the method is changed to: " + str(a))

print("value of global 'a' is: " + str(a))

test_method()
print("Did the value of global 'a' change? " + str(a))