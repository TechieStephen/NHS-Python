#RETURN STATEMENT IN FUNCTIONS
'''
Sometimes when we call a function it basically
executes and perform a task

But there are times you want a function to give
information back after executing -- this is what
the return keyword helps us do in python.

---------------
the return keyword allows python to return information
from a function
---------------

let's write a simple python program to function
a number

///code
def cube(num):
    num*num*num

cube(3)
///

note that nothing happens

///code
def cube(num):
    return num*num*num

cube(3)
///

note that we now get a result

So we basically give information to a function using
parameters and we get information back using
the return statement

NOTE: You can put any code after the return
statement in a function.

------------
You can return any data type you want
'''