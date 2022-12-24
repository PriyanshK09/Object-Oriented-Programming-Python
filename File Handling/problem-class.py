file = open("./File Handling/text1.txt", "r")
print(file.read())
file.close()

file = open("./File Handling/text2.txt", "w")
content = file.write("I am interested in Coding")
file.close()

file = open("./File Handling/text2.txt", "r")
print(file.read())
file.close()

# By using file.close we can close the file
# This way we are making sure that the file is closed properly even if exception is raised that stops the execution of the program