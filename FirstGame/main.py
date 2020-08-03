print("Welcome to LameGame!")
age  = int(input("How old are you "))

if age >= 8:
    print("You are old enough to play this game!")
    wantToPlay = input("Do you want to play this game? ").lower()
    if wantToPlay == "yes":
        print("Awesome! Have fun!")
    else:
        print("Oh, okay then, see you later!")
else:
    print("Sorry but you aren't old enough to play this game")