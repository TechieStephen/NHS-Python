#A GUESSING GAME IN PYTHON
print("I GO UP BUT NEVER COME DOWN")
print("What am i?")
print()

answer = "age"
lives = 3
user_answer = input("Enter your Answer: ")

while lives > 0:
    #check if secret_word == to user_anwser
    if answer.lower() != user_answer.lower():
       print("----Sorry try Again----")
       print(f"You have {lives} lives left")
       print("---------------------")
       print()
       user_answer = input("Enter your Answer: ")
       print()
    else:
        print("---HURRAY!!  YOU WIN!---")
        break

    #decreases live by 1
    lives -= 1 

else:
    print("OUCH!!!!! YOU RAN OUT OF TRIALS")
    
#ohienstephen