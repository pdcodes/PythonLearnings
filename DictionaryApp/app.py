# Load our data
import json

data = json.load(open("data.json"))

# Figure out which word to look up
word = input("Please enter a word: ")

# Return our definition
print(data[word])