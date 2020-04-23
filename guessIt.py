import random

flag = True
while flag:
    userName = input("What is your name? ")
    print(f"Let's play {userName} ")
    mode = str(input('Choose your mode of play: (E/M/H) for Easy, Medium and Hard respectively: '))

    if mode == "E":
        print("This is an easy mode")
        number = random.randint(1,10)
        count = 1
        totalCount = 6

        while(count <= totalCount):
            guess = int(input("Enter a number between 1 to 10: "))
            if guess == number:
                print(f"Weldone {userName}, you got it right ")
                break
            else:
                 print(f"That was wrong, and you have {totalCount - count} guesses left")
            count += 1
            continue
        print("Game Over")

    else:
        print("Invalid, try again")

    if mode == "M":
        print("This is a medium mode")
        number = random.randint(1,20)
        count = 1
        totalCount = 4
        while(count <= totalCount):
            guess = int(input("Enter a number between 1 to 20: "))
            if guess == number:
                print(f"Weldone {userName}, you got it right ")
                break
            else:
                 print(f"That was wrong, and you have {totalCount - count} guesses left")
                 count += 1
                 continue
        print("Game Over")
    else:
        print("Invalid, try again")

    if mode == "H":
        print("This is a hard mode")
        number = random.randint(1,50)
        count = 1
        totalCount = 3
        while(count <= totalCount):
            guess = int(input("Enter a number between 1 to 50: "))
            if guess == "number":
                print(f"Weldone {userName}, you got it right ")
                break
            else:
                 print(f"That was wrong, and you have {totalCount - count} guesses left")
                 count += 1
                 continue
        print("Game Over")
    else:
        print("Invalid, try again")

flag = False
print("Game over, try again")
