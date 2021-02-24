import random
import time
import os

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

nouns = {
    "alphabet": ["Alphabet", "das"],
    "monkey": ["Affe", "der"],
    "ant": ["Ameise", "die"],
    "banana": ["Banane", "die"],
    "boat": ["Boot", "das"],
    "bus": ["Bus", "der"],
    "CD": ["CD", "die"],
    "camp": ["Camp", "das"],
    "roof": ["Dach", "das"],
    "lady": ["Dame", "die"],
    "elephant": ["Elephant", "der"],
    "donkey": ["Esel", "der"],
    "strawberry": ["Erdbeere", "die"],
    "window": ["Fenster", "das"],
    "factory": ["Fabrik", "die"],
    "violin": ["Geige", "die"],
    "guitar": ["Gitarre", "die"],
    "heart": ["Herz", "das"],
    "dog": ["Hund", "der"],
    "house": ["Haus", "das"],
    "hedgehog": ["Igel", "der"],
    "island": ["Insel", "die"],
    "boy": ["Junge", "der"],
    "jacket": ["Jacke", "die"],
    "yacht": ["Yacht", "die"],
    "cook": ["Koch", "der"],
    "cheese": ["Käse", "der"], # ä
    "king": ["König", "der"], # ö
    "teacher": ["Lehrer", "der"],
    "lion": ["Löwe", "der"], # ö
    "lamp": ["Lampe", "die"],
    "lamb": ["Lamm", "das"],
    "moon": ["Mond", "der"],
    "coat": ["Mantel", "der"],
    "mouse": ["Maus", "die"],
    "night": ["Nacht", "die"],
    "fog": ["Nebel", "der"],
    "fruit": ["Obst", "das"],
    "nose": ["Nase", "die"],
    "grandpa": ["Opa", "der"],
    "orange": ["Orange", "die"],
    "horse": ["Pferd", "das"],
    "pepper": ["Paprika", "der"],
    "square": ["Quadrat", "das"],
    "slide": ["Rustche", "die"],
    "radio": ["Radio", "das"],
    "rain": ["Regen", "der"],
    "sun": ["Sonne", "die"],
    "bag": ["Sack", "der"],
    "juice": ["Saft", "der"],
    "tomato": ["Tomate", "die"],
    "table": ["Tisch", "der"],
    "door": ["Tür", "die"], # ü
    "clock": ["Uhr", "die"],
    "subway": ["U-Bahn", "die"],
    "bird": ["Vogel", "der"],
    "vase": ["Vase", "die"],
    "wine": [ "Wein", "der"],
    "water": ["Wasser", "das"],
    "forest": ["Wald", "der"],
    "father": ["Vater", "der"],
    "yoga": [ "Yoga", "das"],
    "yard": ["Yard", "das"],
    "zebra": ["Zebra", "das"],
    "tooth": ["Zahn", "der"],
    "zoo": ["Zoo", "der"],
    "anger": ["Ärger", "der"], # Ä
    "oil": ["Öl", "das"], # Ö
    "exercise": ["Übung", "die"], # Ü
    "foot": ["Fuß", "der"], # ß
    "egg": ["Ei", "das"],
    "ladder": ["Leiter", "die"],
    "bucket": ["Eimer", "der"],
    "owl": ["Eule", "die"],
    "pig": ["Schwein", "die"],
    "street": ["Straße", "die"], # ß
    "sport": ["Sport", "der"],
    "game": ["Spiel", "das"],
    "books": ["Bücher", "die"], # ü
    "blanket": ["Decke", "die"],
    "piece": ["Stück", "das"], # ü
    "place": ["Platz", "der"],
    "knee": ["Knie", "das"],
    "kitchen": ["Küche", "die"],
    "child": ["Kind", "das"],
    "man": ["Mann","der"],
    "woman": ["Frau","die"],
    "cupboard": ["Schrank", "der"],
    "cat": ["Katze", "die"],
    "cup/mug": ["Tasse", "die"],
    "glass": ["glas", "das"],
    "plate": ["Teller", "der"],
    "shelf": ["Regal", "das"],
    "tree": ["Baum", "der"],
    "pen/pencil": ["Stift", "der"],
    "bicycle": ["Fahrrad", "das"],
}
verbs = {
    "come": ["kommen"],
    "eat": ["essen"],
    "steal": ["stehlen"],
    "see": ["sehen"],
    "go/walk": ["gehen"],
    "know": ["wissen"],
    "do/make": ["machen"],
    "say": ["sagen"],
    "read": ["lesen"],
    "play": ["spielen"],
    "need/require": ["brauchen"],
    "buy": ["kaufen"],
    "to shop": ["einkaufen"],
    "find": ["finden"],
    "search": ["suchen"],
    "help": ["helfen"],
    "want/would like": ["möchten"],
    "to taste": ["schmecken"],
    "to get/obtain": ["bekommen"],
    "talk": ["reden"],
    "tell off": ["quatschen"],
    "to chat": ["unterhalten"],
    "to start": ["anfangen"],
    "to arrive": ["ankommen"],
    "to call/phone": ["anrufen"],
    "get up": ["aufstehen"],
    "begin": ["beginnen"],
    "stay": ["bleiben"],
    "bring/take": ["bringen"],
    "think": ["denken"],
    "allowed to": ["dürfen"],
    "drive": ["fahren"],
    "to catch": ["fangen"],
    "watch TV": ["fernsehen"],
    "fly": ["fliegen"],
    "give": ["geben"],
    "can/be able": ["können"],
    "like/want": ["mögen"],
    "must": ["müssen"],
    "to take": ["nehmen"],
    "call": ["rufen"],
    "swim": ["schwimmen"],
    "sing": ["singen"],
    "should": ["sollen"],
    "stand": ["stehen"],
    "meet": ["treffen"],
    "drink": ["trinken"],
    "understand": ["verstehen"],
    "hurt": ["wehtun"],
    "want": ["wollen"],
    "do": ["tun"]
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
    "family": ["Familie", "die"],
    "mother": ["Mutter", "die"],
    "father": ["Vater", "der"],
    "daughter": ["Tochter", "die"],
    "son": ["Sohn", "der"],
    "grandmother": ["Großmutter", "die"],
    "grandfather": ["Großvater", "der"],
    "aunt": ["Tante", "die"],
    "uncle": ["Onkel", "der"],
    "sister": ["Schwester", "die"],
    "brother": ["Bruder", "der"],
    "cousin": ["Cousin", "der"],
    "granddaughter": ["Enkelin", "die"],
    "grandson": ["Enkel", "der"],
    "niece": ["Nichte", "die"],
    "nephew": ["Neffe", "der"],
    "wife": ["Ehefrau", "die"],
    "husband": ["Ehemann", "der"],
    "daughter-in-law": ["Schwiegertochter", "die"],
    "son-in-law": ["Schwiegersohn", "der"],
    "mother-in-law": ["Schwiegermutter", "die"],
    "father-in-law": ["Schwiegervater", "der"],
    "brother-in-law": ["Schwager", "der"],
    "sister-in-law": ["Schwägerin", "die"],
    "baby": ["Baby","das"],
    "child": ["Kind","das"],
    "boy": ["Junge","der"],
    "girl": ["Mädchen", "das"], 
    "teenager": ["Jugendliche", "die"],
    "adult": [ "Erwachsene","der"]     
}
foods = {
    "beer": ["Bier", "das", "Biere"],
    "bun": ["Brotchen", "das", "Brötchen"],
    "bread": ["Brot", "das", "Brote"],
    "egg": ["Ei", "das", "Eier"],
    "butter": ["Butter", "die"],
    "tomato": ["Tomate", "die", "Tomaten"],
    "potatoe": ["Kartoffel", "die", "Kartoffeln"],
    "carrot": ["Karotte", "die", "Karotten"],
    "fruit": ["Obst", "das"],
    "vegetable": ["Gemüse", "das"],
    "lettuce/salad": ["Salat", "der"],
    "onion": ["Zwiebel", "die"],
    "garlic": ["Knoblauch", "der"],
    "apple": ["Apfel", "der", "Äpfel"],
    "banana": ["Banane", "die", "Bananen"],
    "orange": ["Orange", "die", "Orangen"],
    "grapes": ["Trauben", "die"],
    "pear": ["Birne", "die", "Birnen"],
    "coffe": ["Kaffee", "der"],
    "tea": ["Tee", "der"],
    "wine": ["Wein", "der"],
    "water": ["Wasser", "das"],
    "yogurt": ["Joghurt", "der"],
    "cheese": ["Käse", "der"],
    "cream": ["Sahne", "die"],
    "milk": ["Milch", "die"],
    "meat/flesh": ["Fleisch", "das"],
    "sausage": ["Wurst", "die"],
    "pork": ["Schweinefleisch", "das"],
    "beef": ["Rindfleisch", "das"],
    "chicken": ["Hänchenfleisch", "das"],
    "lamb": ["Lammfleisch", "das"],
    "fish": ["Fisch", "der"],
    "salt": ["Salz", "das"],
    "pepper": ["Pfeffer", "das"],
    "sugar": ["Zucker", "der"],
    "cake": ["Kuchen", "der"],
    "pasta/noodles": ["Nudeln", "die"],
    "rice": ["Reis", "der"],
    "flour": ["Mehl", "das"],
    "supermarket": ["Supermarkt", "der"],
    "shop": ["Laden", "der"],
    "bakery": ["Bäckerei", "die"],
    "market": ["Markt", "der"],
    "butcher's shop": ["Merzgerei", "der"],
    "flower shop": ["Blumenladen", "der"],
    "man seller": ["Verkäufer", "der"],
    "woman seller": ["Verkäuferin", "die"],
    "kilo": ["Kilogramm"],
    "liter": ["Liter", "der"],
    "bottle": ["Flasche", "die","Flaschen"],
    "pack/package": ["Packung", "die", "Packungen"],
    "cup": ["Becher", "der"],
    "can": ["Dose", "die", "Dosen"],
    "How much does is cost?": ["Wie viel kostet"],
    "Anything else?": ["Sonst noch etwas"],
    "This makes (smetka)": ["Das macht dann"],
    "tastes good": ["schmeckt gut"],
    "menu": ["Speisekarte","die"],
    "starter": ["Vorspeise","die"],
    "soup": ["Suppe","die"],
    "main course": ["Haupgericht","das"],
    "dessert": ["Nachtisch","der"],
    "jam": ["Konfitüre","die"],
    "ham": ["Schinken","der"],
    "juice": ["Saft","der"],
    "drinks": ["Getränke","die"],
    "breakfast": ["Früstück","das"],
    "slice": ["Scheibe","die"],
    "straw": ["Strohhalm","der"],
    "scrambled eggs": ["Rührei","das"],
    "pancakes": ["Pfannkuchen","der"],
    "gin": ["Gin","der"],
    "vodka": ["Wodka","der"],
    "whiskey": ["Whisky","der"],
    "rum": ["Rum","der"],
    "liqueur": ["Likör","der"],
    "mayonnaise": ["Majonäse","die"],
    "vinegar": ["Essig","der"],
    "sauce": ["Soße","die"],
    "mashed": ["püriert"],
    "baked": ["gebacken"],
    "fried": ["gebraten"],
    "peanut": ["Erdnuss","die"],
    "cashew": ["Cashewnuss","die"],
    "hazelnut": ["Haselnuss","die"],
    "almond": ["Mandel","die"],
    "peach": ["Pfirsich","der"],
    "pineapple": ["Ananas","die"],
    "aprikot": ["Aprikose","die"],
    "tangarine/clementine": ["Mandarine","die"],
    "lemon": ["Zitrone","die"],
    "aubergine/eggplant": ["Aubergine","die"],
    "mushroom": ["Pilz","der"],
    "pumpkin": ["Kürbis","der"],
    "cucumber": ["Gurke","die"],
    "coconut": ["Kokosnuss","die"],
}
personalInfo = {
    "flat/apartment": ["Wonung", "die"],
    "age": ["Alter", "das"],
    "birthplace": ["Geburtsort", "der"],
    "home country": ["Heimatland", "das"],
    "city/town (where you live)": ["Wohnort", "der"],
    "post/zip number": ["Postleintzahl", "die"],
    "divorced": ["geschieden"],
    "married": ["verheiratet"],
    "widowed": ["verwitwet"],
    "capital": ["Hauptstadt"]
}
Wquest = {
    "Where": ["Wo"],
    "Who": ["Wer"],
    "Where for a direction": ["Wohin"],
    "What": ["Was"],
    "How": ["Wie"],
    "When": ["Wann"],
    "How much": ["Wieviel"],
    "Which": ["Welche"],
    "From where": ["Woher"]
} 
importantWords = {
    "something/anything": ["etwas"],
    "more": ["mehr"],
    "for": ["für"],
    "or": ["oder"],
    "also": ["auch"],
    "so/therefore": ["also"],
    "still/yet/even": ["noch"],
    "by/of/from": ["von"],
    "in": ["in"],
    "at the/in the": ["im"],
    "here": ["hier"],
    "late": ["spät"],
    "later/after": ["später"],
    "enough": ["genung"],
    "money": ["Geld", "das"],
    "today": ["heute"],
    "nowadays": ["heutzutage"],
    "about/by": ["über"],
    "with": ["mit"],
    "nonsense": ["quatsch"],
    "once again": ["noch ein Mal"],
    "example": ["Beispiel"],
    "for example": ["zum Beispiel"],
    "almost": ["fast"],
    "North": ["Norden", "der"],
    "East": ["Osten", "der"],
    "South": ["Süden", "der"],
    "West": ["Westen", "der"],
    "slolwy": ["langsam"],
    "no idea": ["keine Ahnung"],
    #"": [""],
    #"": [""],
    #"": [""],
    #"": [""],
    #"": [""],
    #"": [""],
    #"": [""],
    #"": [""],
    #"": [""],
    #"": [""],
    #"": [""],
    #"": [""],
    #"": [""],
}

testedWords = []
listWithCoices = [("Nouns", nouns), ('Verbs', verbs), ("Introducing phrases", introducing), ("Greetings",greeting), ("Countries and Nationalities",countries), ("Family",family), ("Foods", foods),
("Personal information", personalInfo), ("W questions",Wquest),("Important words",importantWords)]

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
            wrongWords += 1
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