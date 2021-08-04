#fname, lname, nationality, phone, address
f_name = input('Enter your first name: ')
l_name = input('Enter your last name: ')
nation = input('Enter your Nationality: ')
phone = input('Enter your Phone Number: ')
address = input('Enter your address: ')

file = open('record.txt', 'w')
user_data = f'''
Fisrt Name : {f_name}
Last Name : {l_name}
Nationality : {nation}
Phone Number : {phone}
Address : {address}
'''
file.write(user_data)




# name = input('Enter Name')
# activation_code = input('Enter Activation Code number')
# user_data = f'Name:{name}\nActivation_Code:{activation_code}'
# file = open('user360.txt', 'w')
# file.write(user_data)

activation_code = 'USER360_9007'
file = open('user360.txt', 'r')
user_data = file.readlines()
x = user_data[1]
a = x.split(':')
# x = user_data[1].split(':')[1]

if x == activation_code:
    print('SUCCESSS')
else:
    print('Invalid Code')#list mutable


#list 
names = ['Joy', 'Sarah', 9]
for name in names:
    print(name)

# Turple Immutable
coordinates = (4, 5)
for x in coordinates:
    print(x)

#Dictionary
car = {
    'brand':'Ford',
    'desc': 'a blue Ford explorer',
    'color': 'Blue'
}
for x in car:
    print(car[x])
   
#ohienstephen

#print numbers from 1-20
x = 1
while x <= 20:
    print(x)
    x += 1 #x = x+1

for x in range(1,21):
    print(x)
    
#ohienstephen


#problem i am hungry
is_hungry = True

rice_ready = False

if is_hungry and rice_ready:
    print('Eat Rice')
else:
    print('Hunger go beat you eeeehh')
    
#ohienstephen

    
