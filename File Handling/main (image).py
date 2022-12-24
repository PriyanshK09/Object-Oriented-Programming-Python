file = open("./File Handling/python.jpg", "rb")
data = file.read()

# Wrtire the data to a new file
file = open("./File Handling/python_copy.jpg", "wb")
file.write(data)
file.close()

