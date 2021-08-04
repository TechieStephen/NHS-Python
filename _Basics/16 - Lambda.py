#Lambda
'''
A lambda function is a small anonymous function.
A Lambda function is a nameless function

lambda functions can take any number of
arguments, but can only have one expression.

The expression in a lambda function is executed
and the result returned.

EXAMPLE:
///Code
lambda_function = lambda x : x * 10
print(lambda_function(5))
///

EXAMPLE:
///Code
lambda_function = lambda a,b : a + b
print(lambda_function(5,6))
///
'''


'''
///Code

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

///


Use lambda functions when an anonymous function is required for a 
short period of time.
'''