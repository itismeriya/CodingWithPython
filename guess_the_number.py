import random
target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or quit(Q): ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("sucess  :)")
        break
    elif(userChoice < target):
        print("you have guessed small number than  target, try again")
    else:
        print("you have guessed big number than target , try again ")

print("game over -------!!") 