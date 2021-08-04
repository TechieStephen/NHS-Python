#DICTIONARIES
''''''
'''
A dictionary is a collection which is unordered, 
changeable and indexed. In Python dictionaries are 
written with curly brackets, and they have keys 
and values.

Dictionaries are key value pair

------------------------------------------
EXAMPLE:    
///Code
months = {
    "Jan" : "January",
    "Mar" : "March",
    "Apr" : "April"
}
///
------------------------------

------------------------------
EXAMPLE 2:
Creates and print a dictionary:

///Code
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": Black
}
print(car)
///
--------------------------------------



NOTE: All of the keys have to be unique



HOW TO ACCESS A SPECIFIC KEY 
OR VALUE IN A DICTIONARY

You can access the items of a dictionary by referring 
to its key name, inside square brackets:

---------------------------------
EXAMPLE:
///Code
months = {
    "Jan" : "January",
    "Mar" : "March",
    "Apr" : "April"
}
print(months['Jan'])
///

--------------------------------------

USING THE GET FUNCTION
The get function can also return a 
default value if you enter an invalid key

---------------------------------
EXAMPLE:
///Code
months = {
    "Jan" : "January",
    "Mar" : "March",
    "Apr" : "April"
}
print(months.get('Jan'))
///

--------------------------------------

NOTE: The get function returns 'none' when
you try to access a key that doesn't exits.
You can change the default value return

---------------------------------
EXAMPLE:
///Code
months = {
    "Jan" : "January",
    "Mar" : "March",
    "Apr" : "April"
}
print(months.get('Luv', 'Not a valid key'))
///

--------------------------------------



CHANGE VALUES IN A DICTIONARY

You can change the value of a specific 
item by referring to its key name:

--------------------------------------------
EXAMPLE:
Change the "year" to 2015:

///Code
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": Black
}
car["year"] = 2018
print(car)
///

--------------------------------------------

DICTIONARY LENGTH
To determine how many items (key-value pairs) 
a dictionary has, use the len() method.

----------------------------------------------
EXAMPLE:
Print the number of items in the dictionary:

///Code
print(len(car))
///
--------------------------------------------


THE KEYS OF A DICTIONARY DO NOT HAVE TO BE 
STRINGS, THEY CAN ALSO BE NUMBERS
'''