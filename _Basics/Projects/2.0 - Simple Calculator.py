'''
_Basics Calculator in Python

TASK: Build a calculator to get tow numbers from a user
adds them together and print out the result

///code
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = num1 + num2
print(sum)
///
NOTICE: We get a wrong ANSWER
fix - convert entered values to int
sum = int(num1) + int(num2)

we can also convert to float
sum = float(num1) + float(num2)

'''

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

sum = float(num1) + float(num2)

print(sum)