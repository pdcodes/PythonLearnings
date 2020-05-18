temperatures = [8.1, 9.3, 11.5]

# Starting with for loops
for temperature in temperatures:
    print(round(temperature))

for letter in "hello":
    print(letter.title())

# Looping through a dictionary
student_grades = {
    "Mary": 9.1,
    "Bob": 12.1,
    "Charlie": 11.1
}

# You've got to specify whether you want the .keys() or .values()
for grades in student_grades.values():
    print(grades)

# Moving to while loops
def convert_to_celsius(temp):
    celsius_temp = temp * (5/9) + 40
    return celsius_temp

counter = 0

while counter < len(temperatures):
    print(convert_to_celsius(temperatures[counter]))
    counter += 1

print(counter)