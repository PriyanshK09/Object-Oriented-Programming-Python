# except : this is used to handle the exception
# this will raise the exception

# else : this is used to execute the code if no exception is raised

# finally : this is used to execute the code no matter what
# this will execute the code no matter what

# try : this is used to test the code for errors
# this will test the code for errors

# 4 blocks of exception handeling are except, else, finally, raise and try

# exception handeling is used to handle the exception
# this will handle the exception

try:
    f = open("testfile.txt", "r")
    try:
        f.write("Write a test line")
    except:
        print("Error")
    finally:
        f.close()
except:
    print("Error: Could not find file or read data")