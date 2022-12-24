file = open("./File Handling/python.jpg", "rb")
file1 = open("./File Handling/python_copy2.jpg", "wb")

for i in file:
    file1.write(i)
    