import datetime
mynow = datetime.datetime.now()
print ("The date and time is:", mynow)


""" Data Types """

# Integers vs. floats
x = 10
y = 10.1
z = "10"

# Lists
student_grades = [8.3, 8.8, 7.5]

# You can use dir() to get info about a class or method
# You can use help() to get info about how to use a class or method

mysum = sum(student_grades) / len(student_grades)
print(mysum)

# Dictionaries
more_student_grades = {
    "Peter": 10.5,
    "Sarah": 9.5
}