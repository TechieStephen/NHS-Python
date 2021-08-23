# FUNCTIONS IN PYTHON
'''
A function is a block of code that  you can run to perform
a simple task.

you can also refer to it as a collection of code that
performs a specific task.

---------------
it's is a re-usable block of code.
it helps you organize your code better
----------------

EXAMPLES OF FUNCTIONS

we've being making use of some of the inbuilt functions
in python

A popular example is the
print function

other examples are string functions
-upper(),
-lower(),
-isupper(),
-islower(),
-type(),
-len(),
index(),
replace()
print()

LETS WRITE OUR OWN FUNCTIONS

to code a function
- start with the def keyword
- give the function a name (just like a variable always
  use descriptive names)
- write an open and close parenthesis and a colon

--------------------
Do not forget the indentation
because poor indentation can make your code not give
you an expected result
--------------------

///code
def say_hi():
    print("Hello Christine")
///

----------------------
The code inside a function will not execute if the
function is not called
----------------------

to call a function write the function name with
an open and closed parenthesis

///code
say_hi()
///

FUNCTION PARAMETER
We can use parameters to make our functions
a bit more powerful

------
a parameter is a piece of information given to a function
------

def say_hi(name):
    print("Hello " + name)
///

///code
say_hi("Stephen")
say_hi("Sarah")
///

You can have as many parameters as you desire

def say_hi(name, age):
    print("Hello " + name + "you are " + age)
///

///code
say_hi("Stephen", 21)
say_hi("Sarah", 23)
///


WHAT DATA TYPE CAN BE PASSED INTO A FUNCTION?
- strings
- numbers
- arrays e.t.c


a python function to sum up two numbers

///code
def def add_numbers(firstNumber, SecondNumber):
    print(firstNumber + SecondNumber)
///


NOTE: As you advance in python you are going to be
using functions more.

Its generally a good idea to always break your
code up into different functions
'''