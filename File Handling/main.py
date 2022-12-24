# Reading the File and Printing the Content

# Open the file in read mode
file = open("./File Handling/text1.txt", "r")

# Read the file
content = file.read()

# Print the content
print(content)

# Check if the file is closed
print(file.closed)

# Close the file
file.close()

# Check if the file is closed
print(file.closed)

# Writing to the File
file = open("./File Handling/text1.txt", "w")
contentW = file.write("This is the new content")
file.close()
file = open("./File Handling/text1.txt", "r")
contentNew = file.read()
print(contentNew)