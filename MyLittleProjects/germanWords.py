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
    "house": ("das", "Haus"),
    "hedgehog": ("der", "Igel"),
    "island": ("die", "Insel"),
    "boy": ("der", "Junge"),
    "jacket": ("die", "Jacke"),
    "yacht": ("die", "Yacht"),
    "cook": ("der", "Koch"),
    "cheese": ("der", "Kase"), # A Umlaut
    "king": ("der", "Konig"), # O umlaut
    "teacher": ("der", "Lehrer"),
    "lion": ("der", "Lowe"), # O Umlaut
    "lamp": ("die", "Lampe"),
    "lamb": ("das", "Lamm"),
    "moon": ("der", "Mond   "),
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
    "slide": ("die", "Rutsche"),
    "radio": ("das", "Radio"),
    "rain": ("der", "Regen"),
    "sun": ("die", "Sonne"),
    "bag": ("der", "Sack"),
    "juice": ("der", "Saft"),
    "tomato": ("die", "Tomate"),
    "table": ("der", "Tisch"),
    "door": ("die", "Tur"), # U umlaut
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
    "anger": ("der", "Arger"), # A umlaut
    "oil": ("das", "Ol"), # O umlaut
    "exercise": ("die", "Ubung"), # U umlaut at the beginnning
    "foot": ("der", "Fuss"),
    "egg": ("das", "Ei"),
    "ladder": ("die", "Leiter"),
    "bucket": ("der", "Eimer"),
    "owl": ("die", "Eule"),
    "pig": ("die", "Schweiz"),
    "street": ("die", "Strasse"), # Estset
    "sport": ("der", "Sport"),
    "game": ("das", "Spiel"),
    "books": ("die", "Bucher"), # U Umlaut
    "blanket": ("die", "Decke"),
    "piece": ("das", "Stuck"), # U umlaut
    "place": ("der", "Platz"),
    "knee": ("das", "Knie")
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