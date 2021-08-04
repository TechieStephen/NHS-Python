#Try Except
'''
When writing Python program it's very common
to encounter different error or exceptions in different
situations.

When this errors occur they can cause our program
to break or mal-function. As developers we can watch out
for certain errors that might occur in our program and
handle them, thereby preventing our code/program from
breaking.

------------------------------------------
EXAMPLE:

///Code
number = int(input("Enter a whole number: "))
print(number)
///

The piece of code above prompts a user to enter a whole
number and then casts the number to an int.

This program will run successfully if a user enters a valid
whole number. On the other hand the program would break if a user
enters anything that's not a valid whole number for example
a string or a float number.

------------------------------------------


In a real world program or application we don't want something like
this to cause our program to break. so we need to handle this
exceptions using a try except block in python.


Exception Handling
When an error occurs, or exception as we call it,
Python will normally stop and generate an error
message.

These exceptions can be handled using the try
statement:

The try block lets you test a block of code for
errors.

The except block lets you handle the error.


The finally block lets you execute code,
regardless of the result of the try and except
blocks.


-------------------------------------------
EXAMPLE:
Using try except block:

///Code

try:
    number = int(input("Enter a whole number: "))
    print(number)
except:
    print("Invalid Input")

///

Notice we can catch the error now when it occurs
---------------------------------------------------------




CATCHING DIFFERENT ERRORS IN PYTHON
Notice in our piece of code above we get a warming line
on the except block saying our exception clause is too
broad. This is because the except block would catch virtually
any type of error in python and as we have noticed from our lessons
so far we know that we get different errors from in different
situations in python.


--------------------------------------------------------
EXAMPLE:
For example when we try to divide by a number by zero we get a
ZeroDivisionError

///Code
result = 20/0
///

to fix this and catch the error we can simple catch the error
based on it type

///Code
try:
    result = 20/0
catch ZeroDivisionError:
    print("Sorry you can't divide a number by Zero'")
///
----------------------------------------------------
'''
number = int(input("Enter a whole number: "))
print(number)
