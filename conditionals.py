def mean(values):
    if type(values) == dict:
        the_mean = sum(values.values()) / len(values)
    else:
        the_mean = sum(values) / len(values)
    return the_mean

student_grades = {
    "Harry": 9.5,
    "Peter": 10.4,
    "Andrew": 11.1
}

soccer_balls = [45.1, 41.2, 40.3]

print("Dict...")
print(mean(student_grades))

print("List...")
print(mean(soccer_balls))