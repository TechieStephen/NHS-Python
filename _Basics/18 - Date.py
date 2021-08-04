#DATE
'''
A date in Python is not a data type of its own,
but we can import a module named datetime to work with dates
as date objects.
'''
'''
----------------------------------------------------------
EXAMPLE:
Import the datetime module and display the current date:

///Code

import datetime #import the datetime module

date = datetime.datetime.now()
print(date)

///

--------------------------------------------------------


The date contains year, month, day, hour, 
minute, second, 
and microsecond.

The datetime module has many methods 
to return information about the date object.


------------------------------------------------------
EXAMPLE
Return the year and name of weekday:

///Code

import datetime

date = datetime.datetime.now()

print(date.year)
print(date.strftime("%A"))

///
----------------------------------------------------


MAKE A DATE OBJECTS

To create a date, we can use the datetime() 
class (constructor) of the datetime module.

The datetime() class requires three parameters 
to create a date: year, month, day.


----------------------------------------------------

EXAMPLE:
Create a date object:

///Code

import datetime
date = datetime.datetime(2022, 3, 21)

print(date)

///

--------------------------------------------------


NOTE: The datetime() class also takes 
parameters for time and timezone 
(hour, minute, second, microsecond, tzone), 
but they are optional, and has a default 
value of 0, (None for timezone).

----------------------------------------------------

The strftime() Method
The datetime object has a method for formatting date 
objects into readable strings.

The method is called strftime(), and takes 
one parameter, format, to specify the format 
of the returned string:

--------------------------------------------------------
EXAMPLE
Display the name of the month:

///Code

import datetime

date = datetime.datetime(2015, 2, 8)
print(date.strftime("%B"))

///
'''

'''
REFERENCES:
https://www.w3schools.com/python/python_datetime.html

'''