def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

# Take the user input and convert to a float
user_input = float(input("Enter temperature: "))
print(weather_condition(user_input))

# You can also convert a value to an int using int()