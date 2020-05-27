# You import a module using the following import statement
import time
import os

while True: 
    if os.path.exists("Files/new.txt"):
        with open("Files/new.txt") as file:
            print(file.read())
    else:
        print("File does not exist!")
    time.sleep(5)