# File processing begins with opening the file
myfile = open("Files/original.txt")
content = myfile.read()

# You should always get in the habit of closing the file!
myfile.close()

# Note: you cannot perform operations on a closed file

# Then you can print the contents of the file using the read() method
print(content)

# You can also open a file using a with block
with open("Files/original.txt") as newfile:
    new_content = newfile.read()

print(new_content)

# The with block will close the file automatically, which makes things simpler

# We'll now write to a new file
with open("Files/new.txt", "w") as writefile:
    writefile.write("Green\nOrange\n")
    writefile.write("Blue")

print(open("Files/new.txt").read())

# Now we're going to append existing content to a file
with open("Files/new.txt", "a+") as colors:
    colors.write("\nBlack\nWhite")
    colors.seek(0)
    printcolors = colors.read()

print(printcolors)

"""
Some additional notes:
Python is always reading and printing from where the cursor is;
Opening a file has a number of different modes that can be used for diff purposes;
The .seek() method allows you to a seek to a particular index value of the string data that is returned from opening a file
"""