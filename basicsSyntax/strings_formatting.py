city = "nyc"
event = "show"

print("Welcome to " + city + " and enjoy the " + event)

print("Welcome to %s and enjoy the %s" % (city, event))  # percents are placeholders, then you give the variables at the end

print("Welcome to %s" % city)  # if its just one, you dont need the parens