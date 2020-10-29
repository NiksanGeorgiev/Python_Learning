import random

#Variables
absoluteTotalWords = 0
absoluteTotalWrongWords = 0
totalWords = 0
wrongArticles = 0
wrongWords = 0
nouns = {
    "alphabet": ("das", "Alphabet"),
    "monkey": ("der", "Affe"),
    "ant": ("die", "Ameise"),
    "banana": ("die", "Banane"),
    "boat": ("das", "Boot"),
    "bus": ("der", "Bus"),
    "CD": ("die", "CD"),
    "camp": ("das", "Camp"),
    "roof": ("das", "Dach"),
    "lady": ("die", "Dame"),
    "elephant": ("der", "Elephant"),
    "donkey": ("der", "Esel"),
    "strawberry": ("die", "Erdbeere"),
    "window": ("das", "Fenster"),
    "factory": ("die", "Fabrik"),
    "violin": ("die", "Geige"),
    "guitar": ("die", "Gitarre"),
    "heart": ("das", "Herz"),
    "dog": ("der", "Hund"),
    "house": ("das", "Haus"),
    "hedgehog": ("der", "Igel"),
    "island": ("die", "Insel"),
    "boy": ("der", "Junge"),
    "jacket": ("die", "Jacke"),
    "yacht": ("die", "Yacht"),
    "cook": ("der", "Koch"),
    "cheese": ("der", "Käse"), # ä
    "king": ("der", "König"), # ö
    "teacher": ("der", "Lehrer"),
    "lion": ("der", "Löwe"), # ö
    "lamp": ("die", "Lampe"),
    "lamb": ("das", "Lamm"),
    "moon": ("der", "Mond"),
    "coat": ("der", "Mantel"),
    "mouse": ("die", "Maus"),
    "night": ("die", "Nacht"),
    "fog": ("der", "Nebel"),
    "fruit": ("das", "Obst"),
    "nose": ("die", "Nase"),
    "grandpa": ("der", "Opa"),
    "orange": ("die", "Orange"),
    "horse": ("das", "Pferd"),
    "pepper": ("der", "Paprika"),
    "square": ("das", "Quadrat"),
    "slide": ("die", "Rustche"),
    "radio": ("das", "Radio"),
    "rain": ("der", "Regen"),
    "sun": ("die", "Sonne"),
    "bag": ("der", "Sack"),
    "juice": ("der", "Saft"),
    "tomato": ("die", "Tomate"),
    "table": ("der", "Tisch"),
    "door": ("die", "Tür"), # ü
    "clock": ("die", "Uhr"),
    "subway": ("die", "U-Bahn"),
    "bird": ("der", "Vogel"),
    "vase": ("die", "Vase"),
    "wine": ("der", "Wein"),
    "water": ("das", "Wasser"),
    "forest": ("der", "Wald"),
    "father": ("der", "Vater"),
    "yoga": ("das", "Yoga"),
    "yard": ("das", "Yard"),
    "zebra": ("das", "Zebra"),
    "tooth": ("der", "Zahn"),
    "zoo": ("der", "Zoo"),
    "anger": ("der", "Ärger"), # Ä
    "oil": ("das", "Öl"), # Ö
    "exercise": ("die", "Übung"), # Ü
    "foot": ("der", "Fuß"), # ß
    "egg": ("das", "Ei"),
    "ladder": ("die", "Leiter"),
    "bucket": ("der", "Eimer"),
    "owl": ("die", "Eule"),
    "pig": ("die", "Schwein"),
    "street": ("die", "Straße"), # ß
    "sport": ("der", "Sport"),
    "game": ("das", "Spiel"),
    "books": ("die", "Bücher"), # ü
    "blanket": ("die", "Decke"),
    "piece": ("das", "Stück"), # ü
    "place": ("der", "Platz"),
    "knee": ("das", "Knie")
}
verbs = {
    "come": "kommen",
    "eat": "essen",
    "steal": "stehlen",
    "see": "sehen",
    "go/walk": "gehen"
}
introducing = {
    "What is your name?(with Name)": "Wie is dein Name",
    "My name is(with Name)": "Mein Name ist",
    "Who are you?": "Wer bist du",
    "I am": "Ich bin",
    "What is your name?": "Wie heißt du",
    "My name is": "Ich heiße",
    "How old are you?": "Wie alt bist du",
    "I am 17 years old": "Ich bin 17 Jahre alt",
    "Which languages do you speak?": "Welche Sprachen sprichst du",
    "I speak English and a little German": "Ich spreche Englisch und ein wenig Deutsch",
    "How are you?": "Wie geht es dir",
    "I am fine": "Es geht mir gut",
    "Where are you from?": "Woher kommst du",
    "I come from Bulgaria": "Ich komme aus Bulgarien"
}
testedWords = []
listWithCoices = [("Nouns", nouns), ('Verbs', verbs), ("Introducing phrases", introducing)]

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


def Examine(wordsDict, isNoun= False):
    global totalWords
    global wrongWords
    global wrongArticles
    global testedWords
    global absoluteTotalWrongWords
    global absoluteTotalWords

    if len(testedWords) == len(wordsDict):
        print("You have been tested on every word!")
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
    randWord = random.choice(list(wordsDict.keys()))
    while randWord in testedWords:
        randWord = random.choice(list(wordsDict.keys()))
    else:
        testedWords.append(randWord)
    totalWords += 1

    print(randWord)
    wordInGerman =''
    wrong = False
    if isNoun:
        article, wordInGerman = wordsDict[randWord]
        userInputArticle = input('Article: ')
        while article != userInputArticle.strip():
            print('Wrong!')
            wrong = True
            userInputArticle = input('Article: ')
        if wrong:
            wrongArticles += 1
    else:
        wordInGerman = wordsDict[randWord]
    userInput = input('Word in German: ')
    wrong = False
    if userInput == "": 
        print("The right words is: ", wordInGerman)
        wrongWords += 1
        return True
    if isNoun:
        userInput = userInput.capitalize()
    counter = 1
    while wordInGerman != userInput.strip() and counter < 3:
        print('Wrong!')
        wrong = True
        userInput = input('Word in German: ')
        if isNoun:
            userInput = userInput.capitalize()
        counter += 1
        if userInput == "":
            print("The right words is: ", wordInGerman)
            return True
    if wrong:
        print("The right words is: ", wordInGerman)
        wrongWords += 1
    print('Correct!')
    print()
    return True

def ChoiceMenu():   
    wordDict = {}
    print('Categories:')

    for i in range(len(listWithCoices)):
        name, dictoray = listWithCoices[i]
        print('{}.'.format(i+1), name)

    while True:
        try:
            choice = int(input('Type in the number of your choice: '))
            if choice in range(1,len(listWithCoices) + 1):
                wordDict = listWithCoices[choice-1][1]     
                if choice == 1:
                    return wordDict, True
                return wordDict, False
            else:
                print('Please enter a valid opition!')
        except:
            print('Please enter a whole number!')
        finally:
            print()

#main cycle
on = True
while on:
    wordDict, isNoun = ChoiceMenu()
    passAnotherWord = True
    while passAnotherWord:
        if not Examine(wordDict,isNoun): break
        passAnotherWord = ContinueExaming(isNoun)
    while True:
        print()
        choice = input('Do you want to select another category? (y/n): ')
        print()
        if choice.lower() == 'y':
            break
        elif choice.lower() == 'n':
            print('Words score for the whole session: {}/{}'.format(absoluteTotalWords-absoluteTotalWrongWords, absoluteTotalWords))
            print('Till next time!')
            on = False
            break
        else:
            print('Please enter y or n!')
    