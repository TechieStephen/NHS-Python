#CONDITIONALS IN PYTHON
"""
Python supports the usual logical
conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

These conditions can be used in
several ways, most commonly in
"if statements" and loops.

NOTE THAT ALL THIS CONDITIONS RETURN
A TRUE OR FALSE RESULT
"""


#IF STATEMENTS
'''
if statement are special features in python 
that enables us to write programs 
that can make decisions.

this means that by using if statements 
i can execute a piece code if a 
certain condition or conditions is true 
and execute other code if the 
certain condition or conditions is false

Lets see some common if statement in 
the human world
----------------------------
In the morning
If I am Hungry
    i eat something

----------------------------
I need a pen
If i cant find my pen
    I get a new pen
otherwise
    I get one from my friends

-------------------------------
I need new cloths
If i have more trousers
    I get more shirts
otherwise if i have more shirts
    I get more trousers
otherwise
    I get 3 shirts and 3 trousers

-------------------------------

In the morning
If i am hungry and I have Indomie
    I eat Indomie
otherwise
    I eat Rice
  
------------------------------

i need a male or a tall female
If you are a male or you are tall
    come to my office
otherwise
    just sit where you are



------------------------------

An "if statement" is written by using the if keyword in python.

///code
x = 5
y = 10
if x > y:
    print("y is greater than x")
///



NOTE THAT IF CONDITIONS SHOULD RESULT TO
TRUE OR FALSE VALUES


///code
is_mall = True

if is_mall:
    print("Come to my office")
else:
    print("Stay where you are")

///

--------------------------------------------------

----- INDENTATION
Python relies on indentation (whitespace at the beginning of a line)
to define scope in the code. Other programming languages often use 
curly-brackets for this purpose.

If statement, without indentation (will raise an error):

///code
x = 5
y = 10
if b > a:
print("y is greater than x") # you will get an error
///
---------------------------------------------------






-----ELSE
The else keyword catches anything which isn't caught 
by the preceding conditions.


///code
x = 5
y = 10
if y > x:
    print("y is greater than x")
else:
    print("x is greater than y")
///






---------------Elif
The elif keyword is pythons way of saying "if the previous 
conditions were not true, then try this condition".

///code
x = 5
y = 10
if y > x:
    print("y is greater than x")
elif a == b:
    print("x and y are equal")
///


--------------------------
You can also use the else keyword

///code
x = 5
y = 10
if y > x:
    print("y is greater than x")
elif a == b:
    print("x and y are equal")
else:
    print("x and y are equal")

///






-----AND/OR KEYWORDS

------------------OR-------------------
///code
is_mall = True
is_tall = True

if is_mall or is_tall:
    print("Come to my office")
else:
    print("Stay where you are")

///

----------------AND--------------------
///code
is_mall = True
is_tall = True

if is_mall and is_tall:
    print("Come to my office")
else:
    print("Stay where you are")

///


---------------NOT-----------------
the not keyword is used to negate a boolean value

///code
not(is_tall)
///





CLASS ASSESSMENT
Write a python function to return the largest of three numbers



'''



if is_male or is_female:
    print("Holla")
else:
    print("What are you")
'''
def check_greatest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    elif num1 == num2:
        return "Num1 is eqaul to num2"

print(check_greatest(3000, 300))


is_male = False
is_female = True

if is_male or is_female:
    print("Holla")
else:
    print("What are you")

if is_male and is_female:
    print("Holla")
else:
    print("What are you")

'''