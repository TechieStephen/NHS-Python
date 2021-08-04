'''
_Basics Calculator in Python using If Statements

TASK: Build a more advanced calculator to perform
basic maths operations


///code
print("A calculator to perfrom _Basics")
print("Maths Operations")
print("-----------------------")
print()

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Please enter operator +, -, /, *")
print()
operator = input("Enter Operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Please select a valid operator")

///

'''