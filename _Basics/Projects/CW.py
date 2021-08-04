username = input("Enter your username: ")
password = input("Enter your password: ")

if len(password) == 5:
    usernameFirstFiveCharater = ""
    for x in username:
        usernameFirstFiveCharater = usernameFirstFiveCharater + x
        if username.index(x) == 4:
            break

    if password == usernameFirstFiveCharater:
        print("GOOD TO GO")
    else:
        print("Password must be the first five characters of username")

else:
    print("Password cannot be more than five charaters")

