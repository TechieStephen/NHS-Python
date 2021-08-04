# File Handling
'''
in this class we are going to learn how to
---Open
-------Read
-------Append
-------Write

We use the open() function in python to
work with files.

To open a file using the open() function
you pass in the filename and mode.

There are four different methods (modes)
for opening a file:
"r" - Read - Default value. Opens a file for reading,
error if the file does not exist

"a" - Append - Opens a file for appending, creates the
file if it does not exist

"w" - Write - Opens a file for writing, creates
the file if it does not exist

"x" - Create - Creates the specified file, returns
an error if the file exists

Syntax
To open a file for reading it is enough to specify
the name of the file:

f = open("demofile.txt")
The code above is the same as:

f = open("demofile.txt", "r")
Because "r" for read, and "t" for text are the
default values, you do not need to specify them.

Note: Make sure the file exists, or else you
will get an error.



# Reading a file

file = open("demofile.txt", "r")
# print(file.read())
# print(file.read(15))
# print(file.readlines())
# print(file.readline())

# for x in file:
#     print(x)
file.close()

# Append/Write to an existing file -mode(a,w)

# file = open('demofile.txt', 'a')
# file.write("I added this line with python code")
#
# file = open('demofile.txt', 'r')
# print(file.read())
# file.close()


# Writting
# file = open('demofile.txt', 'w')
# file.write("I added this line with python code")
#
# file = open('demofile.txt', 'r')
# print(file.read())
# file.close()

# Delete a File
import the os module

import os
os.remove('inowant.py')




CLASS PROJCT

result = activation_number == "ROB_YTUGGJGFGHH23HGJG"
print(result)
if activation_number in database:
     print("Ok")
else:
    print("You cracked this app ABI")
'''

database = ["ROB_YTUGGJGFGHH23HGJG", "ROB_YTUGGNBNBGJH898FGFG"]
file = open("employees.txt", "r+")
activation_detail = file.readlines()[-1]

activation_details_array = activation_detail.split(":")
activation_number = activation_details_array[1]

if activation_number in database:
     print("Ok")
else:
    print("You cracked this app ABI")
