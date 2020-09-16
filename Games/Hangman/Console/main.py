import random

#Functions
def printWord():
    for i in range(wordLength):
        if letters[i] == True:
            print(word[i], end = "")
        else:
            print("-", end = "")
    print()


print("Welcome to Hangman!")

attempts = 5
words = list(("apple", "banana", "carrot", "dragon", "egg","fish","green","horseman"))
length = len(words)

word = words[random.randint(0, length - 1)]
wordLength = len(word)

letters = [False] * wordLength
letters[0] = True
letters[wordLength - 1] = True

#Showing the repeating characters
for i in range(wordLength):
    if (word[0] == word[i]) or (word[wordLength - 1] == word[i]):
        letters[i] = True

#The game
printWord()
wordGuessed = False
while not wordGuessed:
    letter = input("Type in a letter: ")
    if (letter in word) and (letter != word[0] and letter != word[wordLength - 1]):
        for i in range(wordLength):
            if (word[i] == letter):
                letters[i] = True
    else:
        attempts-=1
        if (attempts != 0):
            print("You have " + str(attempts) +" attempts left")
        else:
            break
    wordGuessed = True
    for i in range(wordLength):
        if letters[i] == False:
             wordGuessed = False
    printWord()   
                
if wordGuessed == True:
    print("Congratulations you guessed the word!")
else:
    print("Unfortunately you didn't guess the word. Good luck next time!")
