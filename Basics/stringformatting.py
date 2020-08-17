# String formatting
user_input = input("Enter your name: ")
message = "Hello %s!" % user_input
message2 = f"Hello, {user_input}."
# The f"String {}" approach only works for Python 3.6+"

print(message, "\n", message2)

# String formatting with multiple variables
name = input("Enter your first name: ")
surname = input("Enter your last name: ")

new_message = "Hello %s %s!!" % (name, surname)

print(new_message)

# Take the user input and convert to a float
# user_input = float(input("Enter temperature: "))
# print(weather_condition(user_input))
# You can also convert a value to an int using int()