import random
import pyperclip
from time import sleep

letters = [
 ["а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ь","ю","я","1","2","3","4","5","6","7","8","9"]
,["а","b","v","g","d","е","j","z","i","i","k","l","m","n","о","p","r","s","t","u","f","h","c","ch","sh","sht","u","ь","iu","q","1","2","3","4","5","6","7","8","9"]
,["@","","","","","€","","3","","","","","","","0","","","$","7","","","","","4","6","6т","","ь","","","1","2","3","4","5","6","7","8","9"]
]

text = input()
newText = ""
for letter in text:
    if letter != " ":
        num = random.randint(0,2)
        let = letters[0].index(letter.lower())
        capital = random.randint(0,1)
        if letters[num][let] == "":
            num = random.randint(0,1)
        char = letters[num][let]
        if capital == 1:
            char = char.upper()
        newText += char
    else:
        newText += " "
sleep(0.1)
pyperclip.copy(newText)
print(newText)