"""
Tax in US based on states:

Create a method, which takes the state and gross income as arguments
and returns the net income after deducting tax based on the state.

Assume federal tax: 10%
Assume state tax of your residence

You don't have to do this for all states, just take 3-4 to solve the purpose
of the exercise
"""

# def calculate_tax(state, gross):
#     federal_rate = .10
#     state_rate = 0
#
#     if state == "california" or state == "oregon":
#         state_rate = .10
#     elif state == "south carolina":
#         state_rate = .07
#     else:
#         state_rate = .08
#
#     return gross - (gross * (federal_rate + state_rate))
#
# my_check = calculate_tax("california", 1000)
# print(my_check)

#  Better solution:

def calculate_net_income(gross, state):
    """
    Calculate the net income after federal and state tax
    :param gross: Gross Income
    :param state: State name
    :return: Net income
    """
    state_tax = {"CA": 10, "NY": 9, "TX": 0, "NJ": 6}

    # Calculate the net income after federal tax
    net = gross - (gross * .10)

    # Calculate net income after state tax
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("Your net income after all the heavy taxes is: " + str(net))
        return net
    else:
        print("State not in the list")
        return None

calculate_net_income(100000, "CA")