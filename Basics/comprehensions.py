# List comprehension is a way of processing data on the fly

temps = [221, 234, 340, 230]

# Here we are essentially setting new_temps equal to the values
# returned by the for loop
new_temps = [temp / 10 for temp in temps] 

# You can also do this with conditionals
newer_temps = [temp / 10 for temp in temps if temp >= 230]

# This works a bit different when you have an if / else
newish_temps = [temp / 10 if temp >= 230 else 0 for temp in temps]

print(new_temps)
print(newer_temps)
print(newish_temps)