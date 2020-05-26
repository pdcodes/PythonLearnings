# File processing begins with opening the file
myfile = open("original.txt")
content = myfile.read()

# You should always get in the habit of closing the file!
myfile.close()

# Note: you cannot perform operations on a closed file

# Then you can print the contents of the file using the read() method
print(content)

# You can also open a file using a with block
with open("original.txt") as newfile:
    new_content = newfile.read()

print(new_content)

# The with block will close the file automatically, which makes things simpler