import random

print("Welcome to LameGame!")
age  = int(input("How old are you "))

if age >= 8:
    print("You are old enough to play this game!")
    wantToPlay = input("Do you want to play this game? ").lower()

    if wantToPlay == "yes":
        print("Awesome! Have fun!")
        bottom = 0
        top = int(input("Type in number between 0 and which the computer will try to guess yours "))
        while True:
            middle = int((bottom + top) / 2)
            print(middle)
            lowerHigher = input("Lower, higher or correct? ").lower()
            if lowerHigher == "lower":
                top = middle

            elif lowerHigher =="higher":
                bottom = middle

            elif lowerHigher == "correct":
                print("Your number is", middle)
                break

    else:
        print("Oh, okay then, see you later!")

else:
    print("Sorry but you aren't old enough to play this game")

print("That was it. Have a good day!")