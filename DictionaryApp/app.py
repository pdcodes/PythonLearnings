# Import our tools
import json
import difflib

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
        # Check for similar words
        similars = difflib.get_close_matches(word, data.keys())

        # If we found similar words...
        if len(similars) > 0:
            # print(similars)
            # Loop through them and decide which one to use
            i = 0
            while i < len(similars):
                check_similars = input("You entered {}, but did you mean {}? Please enter 'yes' or 'no': ".format(word, similars[i]))
                if check_similars.lower() == "yes":
                    new_word = similars[i]
                    break
                else:
                    i += 1
                    continue
            return data[new_word]
        else:
            return "I'm sorry, I don't know what to do with that word."

# Figure out which word to look up
definition = input("Please enter a word: ")

# Return our definition
print(lookup(definition))