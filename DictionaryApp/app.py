# Import our tools
import json

# Load our data
data = json.load(open("data.json"))

# Set up a function to process our input
def lookup(word):

    # Normalize our input
    w = word.lower()

    # Check if our word exists and respond accordingly
    if w in data.keys():
        return data[w]
    else:
        return "I'm sorry, I don't know what to do with that word."

# Figure out which word to look up
definition = input("Please enter a word: ")

# Return our definition
print(lookup(definition))