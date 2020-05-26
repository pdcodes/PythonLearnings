import time
import os
import pandas

while True:
    if os.path.exists("Files/original.csv"):
        data = pandas.read_csv("Files/original.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist!")
    time.sleep(5)