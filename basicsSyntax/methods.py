"""
If you type the tripe quotes within a code block, python will automatically
add the "param n1, param n2 etc so you can easily document what your function does.
There is no strongly typed data types, including the arguments
"""


def sum_nums(n1, n2):
    """
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums(2, 3)
print(sum1)
print("x"*20)

def isMetro(city):
    l =["sfo", "nyc", "la"]

    if city in l:  # if the argument exists in the list
        return True
    else:
        return False

x = isMetro("phx")
print(x)
