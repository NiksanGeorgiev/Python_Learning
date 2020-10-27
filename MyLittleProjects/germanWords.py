import random

#TODO: New dictionary for and functions for verbs
totalWords = 0
wrongArticles = 0
wrongWords = 0
words = {
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
    "strawbery": ("die", "Erdbeere"),
    "window": ("das", "Fenster"),
    "factory": ("die", "Fabrik"),
    "violin": ("die", "Geige"),
    "guitar": ("die", "Gitarre"),
    "heart": ("das", "Herz"),
    "dog": ("der", "Hund"),
    "house": ("das", "Haus")
}

testedWords = []

def testRandomWord():
    global totalWords
    global wrongArticles
    global wrongWords
    if len(testedWords) == len(words):
        print("You have been tested on every word!")
        return False
    totalWords += 1
    #Choose and print word in english
    randWord = random.choice(list(words.keys()))
    if randWord in testedWords:
        testRandomWord()
    else:
        testedWords.append(randWord)
    print(randWord)
    article, wordInGerman = words[randWord]
    #Input and check the article
    userInputArticle = input('Article: ')
    wrongArticle = False
    while article != userInputArticle:
        print('Wrong!')
        wrongArticle = True
        userInputArticle = input('Article: ')
    if wrongArticle:
        wrongArticles += 1
    #Input and check word
    wrongWord = False
    userInputWord = input('Word in German: ')
    while wordInGerman != userInputWord:
        print('Wrong!')
        wrongWord = True
        userInputWord = input('Word in German: ')
    if wrongWord:
        wrongWords += 1
    print("Correct!")
    print()

    continueTesting = input('Do you want another word? (y/n): ')
    print()
    if continueTesting == 'n':
        return False
    return True
    

passAnotherWord = True
while passAnotherWord:
    passAnotherWord = testRandomWord()
else:
    print('Article Score: {}/{}'.format(totalWords-wrongArticles, totalWords))
    print('Word Score: {}/{}'.format(totalWords-wrongWords, totalWords))