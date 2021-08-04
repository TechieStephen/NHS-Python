'''
A list is a structure in Python that we can use to
store a collection of information.

Just image a variable that can hold multiple or
many values or data...

///code
friends = ["Peter", "James", John]
///

WHAT CAN YOU PUT INSIDE A LIST
- strings
- numbers
- booleans

HOW TO ACCESS ITEMS IN LIST
--print all items
print(friends)

--print specific item
print(friends[2])

this happens because of index which starts at
position 0
so:
friends[0] returns Peter
friends[2] returns John

When you use negative values index its starts indexing
from the last element
e.g
friends[-1] returns John

friends[1:] returns the element or item at index 1
and other elements after it


LOOPING THROUGH A LIST
You can loop through the list items by using a for loop:
Print all items in the list, one by one:
///code
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
///

Check if Item Exists
To determine if a specified item is present
in a list use the in keyword:

Example
Check if "apple" is present in the list:

fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits list")


Add Items
To add an item to the end of the list, use the append() method:

Example
Using the append() method to append an item:

fruit = ["apple", "banana", "cherry"]
fruit.append("orange")
print(fruit)


To add an item at the specified index,
use the insert() method:

Example
Insert an item as the second position:

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)


Example
The pop() method removes the specified
index, (or the last item if index is not specified):

fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)

Example
The del keyword removes the specified index:

fruits = ["apple", "banana", "cherry"]
del fruits[0]
print(fruits)

Example
The del keyword can also delete the list completely:

fruits = ["apple", "banana", "cherry"]
del fruits


The clear() method empties the list:

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)


COPY A LIST
You cannot copy a list simply by typing list2 = list1,
because: list2 will only be a reference to list1,
and changes made in list1 will automatically also be made in
list2.

There are ways to make a copy, one way is to use the
built-in List method copy().

Example
Make a copy of a list with the copy() method:

fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()
fruits.append("Orange")

Another way to make a copy is to use the
built-in method list().

Example
Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

Join Two Lists
There are several ways to join, or concatenate,
two or more lists in Python.

One of the easiest ways are by using the + operator.

Example
Join two list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

Another way to join two lists are by appending all
the items from list2 into list1, one by one:

Example
Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

USING THE LIST
The list() Constructor
It is also possible to use the list() constructor
to make a new list.

///code
fruits = list(("apple", "banana", "cherry")) # note the double round-brackets
print(fruits)
///
'''
