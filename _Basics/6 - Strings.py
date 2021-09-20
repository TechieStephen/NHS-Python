'''
strings are one of the most popularly used
data types in python
strings are always enclosed with quotation
marks ("",'')

string functions
-upper(),
-lower(),
-isupper(),
-islower(),
-type(),
-len(),
index(),
replace(),
'''

name = "Sarah"
print(name.upper())
print(name.lower())

print(name.lower().islower())
print(name.upper().isupper())
print("---------------------------")
print(len(name))

print("---------------------------")
print(name.index("Sa"))

story = "There is a girl called Bola"
print("---------------------------")
print(story[-1])

print("---------------------------")
print(story.replace("Bola", "Tobi"))



