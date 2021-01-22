import random
import time

#Variables
absoluteTotalWords = 0
absoluteTotalWrongWords = 0
absoluteTotalPlurals = 0
absoluteTotalWrongPlurals = 0
totalWords = 0
wrongPlurals = 0
wrongWords = 0
totalPlurals = 0
nouns = {
    "alphabet": ["das", "Alphabet"],
    "monkey": ["der", "Affe"],
    "ant": ["die", "Ameise"],
    "banana": ["die", "Banane"],
    "boat": ["das", "Boot"],
    "bus": ["der", "Bus"],
    "CD": ["die", "CD"],
    "camp": ["das", "Camp"],
    "roof": ["das", "Dach"],
    "lady": ["die", "Dame"],
    "elephant": ["der", "Elephant"],
    "donkey": ["der", "Esel"],
    "strawberry": ["die", "Erdbeere"],
    "window": ["das", "Fenster"],
    "factory": ["die", "Fabrik"],
    "violin": ["die", "Geige"],
    "guitar": ["die", "Gitarre"],
    "heart": ["das", "Herz"],
    "dog": ["der", "Hund"],
    "house": ["das", "Haus"],
    "hedgehog": ["der", "Igel"],
    "island": ["die", "Insel"],
    "boy": ["der", "Junge"],
    "jacket": ["die", "Jacke"],
    "yacht": ["die", "Yacht"],
    "cook": ["der", "Koch"],
    "cheese": ["der", "Käse"], # ä
    "king": ["der", "König"], # ö
    "teacher": ["der", "Lehrer"],
    "lion": ["der", "Löwe"], # ö
    "lamp": ["die", "Lampe"],
    "lamb": ["das", "Lamm"],
    "moon": ["der", "Mond"],
    "coat": ["der", "Mantel"],
    "mouse": ["die", "Maus"],
    "night": ["die", "Nacht"],
    "fog": ["der", "Nebel"],
    "fruit": ["das", "Obst"],
    "nose": ["die", "Nase"],
    "grandpa": ["der", "Opa"],
    "orange": ["die", "Orange"],
    "horse": ["das", "Pferd"],
    "pepper": ["der", "Paprika"],
    "square": ["das", "Quadrat"],
    "slide": ["die", "Rustche"],
    "radio": ["das", "Radio"],
    "rain": ["der", "Regen"],
    "sun": ["die", "Sonne"],
    "bag": ["der", "Sack"],
    "juice": ["der", "Saft"],
    "tomato": ["die", "Tomate"],
    "table": ["der", "Tisch"],
    "door": ["die", "Tür"], # ü
    "clock": ["die", "Uhr"],
    "subway": ["die", "U-Bahn"],
    "bird": ["der", "Vogel"],
    "vase": ["die", "Vase"],
    "wine": ["der", "Wein"],
    "water": ["das", "Wasser"],
    "forest": ["der", "Wald"],
    "father": ["der", "Vater"],
    "yoga": ["das", "Yoga"],
    "yard": ["das", "Yard"],
    "zebra": ["das", "Zebra"],
    "tooth": ["der", "Zahn"],
    "zoo": ["der", "Zoo"],
    "anger": ["der", "Ärger"], # Ä
    "oil": ["das", "Öl"], # Ö
    "exercise": ["die", "Übung"], # Ü
    "foot": ["der", "Fuß"], # ß
    "egg": ["das", "Ei"],
    "ladder": ["die", "Leiter"],
    "bucket": ["der", "Eimer"],
    "owl": ["die", "Eule"],
    "pig": ["die", "Schwein"],
    "street": ["die", "Straße"], # ß
    "sport": ["der", "Sport"],
    "game": ["das", "Spiel"],
    "books": ["die", "Bücher"], # ü
    "blanket": ["die", "Decke"],
    "piece": ["das", "Stück"], # ü
    "place": ["der", "Platz"],
    "knee": ["das", "Knie"],
    "kitchen": ["die", "Küche"],
    "child": ["das", "Kind"],
    "man": ["der", "Mann"],
    "woman": ["die", "Frau"],
    "cupboard": ["der", "Schrank"]
}
verbs = {
    "come": ["kommen"],
    "eat": ["essen"],
    "steal": ["stehlen"],
    "see": ["sehen"],
    "go/walk": ["gehen"]

}
introducing = {
    "What is your name?[with Name]": ["Wie is dein Name"],
    "My name is[with Name]": ["Mein Name ist"],
    "Who are you?": ["Wer bist du"],
    "I am": ["Ich bin"],
    "What is your name?": ["Wie heißt du"],
    "My name is": ["Ich heiße"],
    "How old are you?": ["Wie alt bist du"],
    "I am 17 years old": ["Ich bin 17 Jahre alt"],
    "Which languages do you speak?": ["Welche Sprachen sprichst du"],
    "I speak English and a little German": ["Ich spreche Englisch und ein wenig Deutsch"],
    "How are you?": ["Wie geht es dir"],
    "I am fine": ["Es geht mir gut"],
    "Where are you from?": ["Woher kommst du"],
    "I come from Bulgaria": ["Ich komme aus Bulgarien"]
}
greeting = {
    "Hello": ["Hallo"],
    "Good morning": ["Guten Morgen"],
    "Good day": ["Guten Tag"],
    "Good afternoon/evening": ["Guten Abend"],
    "Good night": ["Gute Nacht"],
    "Welcome": ["Herzlich Willkommen"],
    "It's nice to meet you": ["Es freut mich Sie kennenzulernen"],
    "Goodbye[in person]": ["Auf Wiedersehen"],
    "Goodbye[on the phone]": ["Auf Wiederhören"],
    "Bye": ["Tschüs"],
    "See you soon": ["Bis Bald"]
}
countries = {
    "Germany":["Deutschland"],
    "Austria":["Östereich"],
    "Portugal":["Portugal"],
    "France":["Frankreich"],
    "Great Britan":["Großbritannien"],
    "Japan":["Japan"],
    "South Africa":["Südafrika"],
    "Canada":["Kanada"],
    "China":["China"],
    "Switzerland":["die Schweitz"],
    "Turkey":["die Türkei"],
    "USA":["die USA"],
    "English":["Englisch"],
    "French":["Französisch"],
    "Spanish":["Spanisch"],
    "Italian":["Italienisch"],
    "Chinese":["Chinesisch"],
    "Russian":["Russisch"],
    "German":["Deutsch"]
}
family = {
    "family": ["die", "Familie"],
    "mother": ["die", "Mutter"],
    "father": ["der", "Vater"],
    "daughter": ["die", "Tochter"],
    "son": ["der", "Sohn"],
    "grandmother": ["die", "Großmutter"],
    "grandfather": ["der", "Großvater"],
    "aunt": ["die", "Tante"],
    "uncle": ["der", "Onkel"],
    "sister": ["die", "Schwester"],
    "brother": ["der", "Bruder"],
    "cousin": ["der", "Cousin"],
    "granddaughter": ["die", "Enkelin"],
    "grandson": ["der", "Enkel"],
    "niece": ["die", "Nichte"],
    "nephew": ["der", "Neffe"],
    "wife": ["die", "Ehefrau"],
    "husband": ["der", "Ehemann"],
    "daughter-in-law": ["die", "Schwiegertochter"],
    "son-in-law": ["der", "Schwiegersohn"],
    "mother-in-law": ["die", "Schwiegermutter"],
    "father-in-law": ["der", "Schwiegervater"],
    "brother-in-law": ["der", "Schwager"],
    "sister-in-law": ["die", "Schwägerin"],
    "baby": ["das", "Baby"],
    "child": ["das", "Kind"],
    "boy": ["der", "Junge"],
    "girl": ["das", "Mädchen"], 
    "teenager": ["die", "Jugendliche"],
    "adult": ["der", "Erwachsene"] 
    
}
testedWords = []
listWithCoices = [[("Nouns", nouns)], ('Verbs', verbs), ("Introducing phrases", introducing), ("Greetings",greeting), ("Countries and Nationalities",countries), ("Family",family)]

def time_convert(sec):
  mins = sec // 60
  sec = round(sec % 60)
  
  print("Time Lapsed = {0}:{1}".format(int(mins),sec))

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
        if len(number) == 4:
            if number[0] == "1":
                answer+="eintausend"
            else:
                answer+=numbers1to10[int(number[0])-1] + "tausend"
            number = number[1:4]
        if len(number) == 3:
            if number[0] == "0":
                pass
            elif number[0] == "1":
                answer += "einhundert"
            else:
                answer += numbers1to10[int(number[0])-1] + "hundert"
            number = number[1:3]
        if len(number) == 2:
            if number[0] == "0":
                number = number[1]
            elif number[0] == "1":
                if number == "11":
                    answer += "elf"
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


def Examine(wordsDict, hasPlural= False):
    global totalWords
    global wrongWords
    global wrongPlurals
    global testedWords
    global absoluteTotalWrongWords
    global absoluteTotalWords
    global absoluteTotalWrongPlurals
    global absoluteTotalPlurals
    global totalPlurals

    if len(testedWords) == len(wordsDict):
        print("You have been tested on every word!")
        print('Plural Score: {}/{}'.format(totalPlurals-wrongPlurals, totalPlurals))
        print('Word Score: {}/{}'.format(totalWords-wrongWords, totalWords))
        absoluteTotalWords += totalWords
        absoluteTotalWrongWords += wrongWords
        absoluteTotalPlurals += totalPlurals
        absoluteTotalWrongPlurals += wrongPlurals
        totalWords = 0
        wrongPlurals = 0
        wrongWords = 0
        totalPlurals = 0
        testedWords = []
        return False
    randWord = random.choice(list(wordsDict.keys()))
    while randWord in testedWords:
        randWord = random.choice(list(wordsDict.keys()))
    else:
        testedWords.append(randWord)
    totalWords += 1

    if len(wordsDict[randWord]) == 2:
        hasPlural = True
        totalPlurals += 1
    print(randWord)
    wordInGerman =''
    wrong = False
    wordInGerman = wordsDict[randWord][0]
    userInput = input('Word in German: ')
    counter = 1
    if userInput == "": 
        print("The right words is: ", wordInGerman)
        wrongWords += 1
        counter = 4
    while wordInGerman != userInput.strip() and counter < 3:
        print('Wrong!')
        wrong = True
        userInput = input('Article: ')
        counter += 1
        if userInput == "":
            print("The right words is: ", wordInGerman)
            counter = 4
            wrongWords += 1
            break
    if wrong:
        if counter == 3:
                print("The right word is: ", wordInGerman)
        wrongWords += 1
    if userInput == wordInGerman:
        print('Correct!')
    wrong = False
    if hasPlural:
        wordInGerman, plural = wordsDict[randWord]
        userInput = input('Word: ')
        counter = 1
        if userInput == "": 
            print("The right words is: ", plural)
            wrongPlurals += 1
            counter = 4
        while plural != userInput.strip() and counter < 3:
            print('Wrong!')
            wrong = True
            userInput = input('Word in German: ')
            counter += 1
            if userInput == "":
                print("The right words is: ", plural)
                counter = 4
                break
        if wrong:
            if counter == 3:
                print("The right words is: ", plural)
            wrongPlurals += 1
        if userInput == plural:
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
                return wordDict
            else:
                print('Please enter a valid opition!')
        except:
            print('Please enter a whole number!')
        finally:
            print()

#main cycle
Numbers()
on = True
while on:
    wordDict = ChoiceMenu()
    passAnotherWord = True
    while passAnotherWord:
        if not Examine(wordDict): break
        
    while True:
        print()
        choice = input('Do you want to select another category? (y/n): ')
        print()
        if choice.lower() == 'y':
            break
        elif choice.lower() == 'n':
            print ('Word score for the whole session: {}/{}'.format(absoluteTotalPlurals-absoluteTotalWrongPlurals,absoluteTotalWrongPlurals))
            print('Article score for the whole session: {}/{}'.format(absoluteTotalWords-absoluteTotalWrongWords, absoluteTotalWords))
            print('Till next time!')
            on = False
            break
        else:
            print('Please enter y or n!')