# Playing around with lists a bit more
monday_temps = [4.5, 4.6, 4.8]
print(monday_temps)

print("Appending...")
monday_temps.append(8.7)
print(monday_temps)

print("Clearing...")
monday_temps.clear()
print(monday_temps)

print("Recreating")
monday_temps = [4.5, 4.6, 4.8]

print("Getting index of 4.5...")
print(monday_temps.index(4.5))

# The index method takes addnl parameters that allow
# you to search over a specified range in the list
# This is done by adding the array positions as parameters
# to the .index() method as after the value that you're looking for

print("Getting the item at position #2")
print(monday_temps[1])

"""
Array slices can be implemented using the
syntax array[x:y] where x and y are the start and end position (exclusive)
that denote the range of positions that you want to pull from
"""