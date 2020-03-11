"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""

def sum_nums(n1 = 2, n2 = 4):  # Giving a default value. You can give defaults to one or both
    """
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

sum1 = sum_nums(2, 8)
print(sum1)

no_arguments = sum_nums()
print(no_arguments)

explicit_arguments = sum_nums(n1 = 8, n2 = 20)
print(explicit_arguments)

switcharoo_explicit = sum_nums(n2 = 20, n1 = 8)
print(switcharoo_explicit)