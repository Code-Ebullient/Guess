""" Guessing game program with numbers """
import random

# Loop to start the main program
flag = True
while flag:
    """ Game players needed to be identified by their names """
    userName = input("What is your name? ")
    print(f"Let's play {userName} ")

    # Game levels, each with randint to generate the random number
    mode = str(input('Choose your mode of play: (E/M/H) for Easy, Medium and Hard respectively: '))

    # Easy mode random number generation
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

    # Medium mode random number generation
    elif mode == "M":
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

    # Hard mode random number generation
    elif mode == "H":
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
        print("Invalid, , try again later")
        break

flag = False
print("Game over")
