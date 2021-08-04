# OS MODULE
import os

#Check for Existing File
x = os.path.exists('check')
print(x)

# Delete a directory
os.rmdir('check')