import random
import time
import os
from words import *
#Variables
COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m"
}
absoluteTotalWords = 0
absoluteTotalWrongWords = 0
absoluteTotalArticles = 0
absoluteTotalWrongArticles = 0
absoluteTotalPlurals = 0
absoluteTotalWrongPlurals = 0
totalWords = 0
wrongArticles = 0
wrongWords = 0
totalArticles = 0
totalPlurals = 0
wrongPlurals = 0

testedWords = []
listWithCoices = [
    ("Nouns", nouns),
    ('Verbs', verbs),
    ("Introducing phrases", introducing),
    ("Greetings",greeting),
    ("Countries and Nationalities",countries),
    ("Family",family), ("Foods", foods),
    ("Personal information", personalInfo),
    ("W questions",Wquest),
    ("Important words",importantWords),
    ("Apartment", apartment),
    ("Weather", weather),
    ("Adjectives", adjectives)     
]

def time_convert(sec):
  mins = sec // 60
  sec = round(sec % 60)
  
  print(colorText("[[cyan]]Time taken = [[blue]]{0}:{1}[[cyan]]".format(int(mins),sec)))

def Numbers():
    low = int(input("Choose the lowest number: "))
    high = int(input("Choose the highest number: "))+1
    count = 0
    start_time = time.time()
    while (count < 20):
        number = random.randint(low,high)
        print(number)
        answer = ""
        numbers1to10 = ["eins","zwei","drei","vier","fünf", "sechs","sieben","acht","neun","zehn"]
        number = str(number)

        #Four digit numbers
        if len(number) == 4:
            if number[0] == "1":
                answer+="eintausend"
            else:
                answer+=numbers1to10[int(number[0])-1] + "tausend"
            number = number[1:4]

        #three degit numbers
        if len(number) == 3:
            if number[0] == "0":
                pass
            elif number[0] == "1":
                answer += "einhundert"
            else:
                answer += numbers1to10[int(number[0])-1] + "hundert"
            number = number[1:3]
        #two digit numbers
        if len(number) == 2:
            if number[0] == "0":
                number = number[1]
            elif number[0] == "1":
                if number == "11":
                    answer += "elf"
                elif number == "10":
                    answer += "zehn"
                elif number == "12":
                    answer += "zwölf"
                elif number == "16":
                    answer += "sechzehn"
                elif number == "17":
                    answer += "siebzehn"
                else:
                    answer += numbers1to10[int(number[1])-1]+ "zehn"
            elif number[0] == "2":
                if number[1] == "0":
                    answer += "zwanzig"
                elif number[1] == "1":
                    answer += "einundzwanzig"
                else:
                    answer += numbers1to10[int(number[1])-1]+ "undzwanzig"
            elif number[0] == "3":
                if number[1] == "0":
                    answer += "dreißig"
                elif number[1] == "1":
                    answer += "einunddreißig"
                else:
                    answer += numbers1to10[int(number[1])-1]+ "unddreißig"
            elif number[0] == "6":
                if number[1] == "0":
                    answer += "sechzig"
                elif number[1] == "1":
                    answer += "einundsechzig"
                else:
                    answer += numbers1to10[int(number[1])-1]+ "undsechzig"
            elif number[0] == "7":
                if number[1] == "0":
                    answer += "siebzig"
                elif number[1] == "1":
                    answer += "einundsiebzig"
                else:
                    answer += numbers1to10[int(number[1])-1]+ "undsiebzig"
            else:
                if number[1] == "0":
                    answer += numbers1to10[int(number[0])-1] + "zig"
                if number[1] == "1":
                    answer += "einund" + numbers1to10[int(number[0])-1] + "zig"
                else:
                    answer += numbers1to10[int(number[1])-1] + "und" + numbers1to10[int(number[0])-1] + "zig"
        if len(number) == 1:
            answer += numbers1to10[int(number)-1]
        while answer != input().strip():
            print("Wrong!")
        else:
            print("Correct!")
            count += 1

    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
        
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
          
def ContinueExaming(isNoun= False):
    global totalWords
    global wrongArticles
    global wrongWords
    global testedWords
    global absoluteTotalWrongWords
    global absoluteTotalWords

    while True:    
        continueTesting = input('Do you want another word? (y/n): ')
        print()
        if continueTesting.lower() == 'n':
            if isNoun:
                print('Article Score: {}/{}'.format(totalWords-wrongArticles, totalWords))
            print('Word Score: {}/{}'.format(totalWords-wrongWords, totalWords))
            absoluteTotalWords += totalWords
            absoluteTotalWrongWords += wrongWords
            totalWords = 0
            wrongArticles = 0
            wrongWords = 0
            testedWords = []
            return False
        elif continueTesting.lower() == 'y':
            return True
        else:
            print('Please enter y or n!')
            print()

def Examine(wordsDict, hasArticle= False, hasPlural = False):
    global totalWords
    global wrongWords
    global wrongArticles
    global testedWords
    global absoluteTotalWrongWords
    global absoluteTotalWords
    global absoluteTotalWrongArticles
    global absoluteTotalArticles
    global totalArticles
    global totalPlurals
    global wrongPlurals
    global absoluteTotalPlurals
    global absoluteTotalWrongPlurals

    if len(testedWords) == len(wordsDict):
        print(colorText("[[cyan]]You have been tested on every word!"))
        print(colorText('[[cyan]]Article Score: [[blue]]{}/{}'.format(totalArticles-wrongArticles, totalArticles)))
        print(colorText('[[cyan]]Word Score: [[blue]]{}/{}'.format(totalWords-wrongWords, totalWords)))
        print(colorText('[[cyan]]Plural Score: [[blue]]{}/{}'.format(totalPlurals-wrongPlurals, totalPlurals)))
        absoluteTotalWords += totalWords
        absoluteTotalWrongWords += wrongWords
        absoluteTotalArticles += totalArticles
        absoluteTotalWrongArticles += wrongArticles
        absoluteTotalPlurals += totalPlurals
        absoluteTotalWrongPlurals += wrongPlurals
        totalWords = 0
        wrongArticles = 0
        wrongWords = 0
        totalArticles = 0
        totalPlurals = 0
        wrongPlurals = 0
        testedWords = []
        return False
    randWord = random.choice(list(wordsDict.keys()))
    while randWord in testedWords:
        randWord = random.choice(list(wordsDict.keys()))
    else:
        testedWords.append(randWord)
    totalWords += 1

    if len(wordsDict[randWord]) == 3:
        hasPlural = True
        hasArticle = True
        totalArticles += 1
        totalPlurals += 1

    if len(wordsDict[randWord]) == 2:
        hasArticle = True
        totalArticles += 1

    print(randWord)
    wordInGerman =''
    wrong = False
    wordInGerman = wordsDict[randWord][0]
    userInput = input('Word in German: ')
    counter = 1
    if userInput == "": 
        print("The right words is: ", colorText('[[yellow]]'+ wordInGerman +'[[white]]'))
        wrongWords += 1
        counter = 4

    while wordInGerman != userInput.strip() and counter < 3:
        print(colorText('[[red]]Wrong![[white]]'))
        wrong = True
        userInput = input('Word in German: ')
        counter += 1
        if userInput == "":
            print("The right words is: ", colorText('[[yellow]]'+ wordInGerman +'[[white]]'))
            counter = 4
            break

    if wrong:
        if counter == 3:
                print("The right words is: ", colorText('[[yellow]]'+ wordInGerman +'[[white]]'))
        wrongWords += 1

    if userInput == wordInGerman:
        print(colorText('[[green]]Correct![[white]]'))

    wrong = False
    if hasArticle:
        if hasPlural:
            wordInGerman, article, *_ = wordsDict[randWord]
        else:
            wordInGerman, article = wordsDict[randWord]
        userInput = input('Article: ') 
        counter = 1
        if userInput == "": 
            print("The right words is: ", colorText('[[yellow]]'+ article +'[[white]]'))
            wrongArticles += 1
            counter = 4
        while article != userInput.strip() and counter < 3:
            print(colorText('[[red]]Wrong![[white]]'))
            wrong = True
            userInput = input('Article: ')
            counter += 1
            if userInput == "":
                print("The right words is: ", colorText('[[yellow]]'+ article +'[[white]]'))
                counter = 4
                break
        if wrong:
            if counter == 3:
                print("The right words is: ", colorText('[[yellow]]'+ article +'[[white]]'))
            wrongArticles += 1
        if userInput == article:
             print(colorText('[[green]]Correct![[white]]'))

    if hasPlural:
        wordInGerman, article, plural = wordsDict[randWord]
        userInput = input('Plural: ') 
        counter = 1
        if userInput == "": 
            print("The right words is: ", colorText('[[yellow]]'+ plural +'[[white]]'))
            wrongPlurals += 1
            counter = 4
        while plural != userInput.strip() and counter < 3:
            print(colorText('[[red]]Wrong![[white]]'))
            wrong = True
            userInput = input('Plural: ')
            counter += 1
            if userInput == "":
                print("The right words is: ", colorText('[[yellow]]'+ plural +'[[white]]'))
                counter = 4
                break
        if wrong:
            if counter == 3:
                print("The right words is: ", colorText('[[yellow]]'+ plural +'[[white]]'))
            wrongPlurals += 1
        if userInput == plural:
             print(colorText('[[green]]Correct![[white]]'))
      
    print()
    return True

def ChoiceMenu():   
    wordDict = {}
    print(colorText('[[cyan]]Categories:'))

    for i in range(len(listWithCoices)):
        name, dictonary = listWithCoices[i]
        print(colorText('[[magenta]]{}.'.format(i+1)), name)

    while True:
        try:
            choice = int(input(colorText('[[cyan]]Type in the number of your choice: [[white]]')))
            if choice in range(1,len(listWithCoices) + 1):
                wordDict = listWithCoices[choice-1][1]     
                return wordDict
            else:
                print('Please enter a valid opition!')
        except:
            print('Please enter a whole number!')
        finally:
            print()

#main cycle
#Numbers()
os.system("cls")
start_time = time.time()
on = True
while on:
    wordDict = ChoiceMenu()
    passAnotherWord = True
    while passAnotherWord:
        if not Examine(wordDict): break  
    while True:
        print()
        choice = input(colorText('[[cyan]]Do you want to select another category? (y/n): [[white]]'))
        print()
        if choice.lower() == 'y':
            break
        elif choice.lower() == 'n':
            print (colorText('[[cyan]]Article score for the whole session: [[blue]]{}/{}'.format(absoluteTotalArticles-absoluteTotalWrongArticles,absoluteTotalArticles)))
            print(colorText('[[cyan]]Words score for the whole session: [[blue]]{}/{}'.format(absoluteTotalWords-absoluteTotalWrongWords, absoluteTotalWords)))
            print(colorText('[[cyan]]Plural score for the whole session: [[blue]]{}/{}'.format(absoluteTotalPlurals-absoluteTotalWrongPlurals, absoluteTotalPlurals)))
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed) 
            print(colorText('[[green]]Till next time![[white]]'))
            on = False
            break
        else:
            print('Please enter y or n!')