import re 
import os
import pandas
from flask import render_template

alphabet = {"a":"#D9D9D9", 
            "b":"#D9D9D9", 
            "c":"#D9D9D9", 
            "d":"#D9D9D9", 
            "e":"#D9D9D9", 
            "f":"#D9D9D9", 
            "g":"#D9D9D9", 
            "h":"#D9D9D9", 
            "i":"#D9D9D9", 
            "j":"#D9D9D9", 
            "k":"#D9D9D9", 
            "l":"#D9D9D9", 
            "m":"#D9D9D9", 
            "n":"#D9D9D9", 
            "o":"#D9D9D9", 
            "p":"#D9D9D9", 
            "q":"#D9D9D9", 
            "r":"#D9D9D9", 
            "s":"#D9D9D9", 
            "t":"#D9D9D9", 
            "u":"#D9D9D9", 
            "v":"#D9D9D9", 
            "w":"#D9D9D9", 
            "x":"#D9D9D9", 
            "y":"#D9D9D9", 
            "z":"#D9D9D9"}

inWord = []
notInWord = []
wordPositions = {0:"_", 1: "_", 2: "_", 3: "_", 4: "_"}
storedDFs = []

# creating a pandas dataframe from the dictionary
dictionaryFile = open("fiveLetterWords.txt", "r")
dictionaryDF = pandas.read_csv(dictionaryFile)
dictionaryFile.close()

# creating updatedForm0.html file at start
def starting():
    form = open("templates/form.html", "r")
    uForm = open("templates/updatedForm0.html", "w")
    for line in form:
        uForm.write(line)
    uForm.close()
    form.close() 

# update inWord
def inWordUpdate(letters):
    for letter in letters:
        inWord.append(letter.lower())
        alphabet[letter] = "#FFE175"

# update notInWord
def notInWordUpdate(letters):
    for letter in letters:
        notInWord.append(letter.lower())
        alphabet[letter] = "#FF9292"

# update wordPositions
def wordPositionsUpdate(positions):
    for i in range(0, min(len(positions),5)):
        if(positions[i] != "_"):
            wordPositions[i] = positions[i]
            alphabet[positions[i]] = "#6DE796"

# update the form appearance 
colorExp = re.compile(r'class="letter"')
fiveExp = re.compile(r'class="oneLetter"')
def updateForm(number):
    form = open("templates/form.html", "r")
    os.remove(str.format("templates/updatedForm{number}.html", number=number-1))
    uForm = open(str.format("templates/updatedForm{number}.html", number=number), "w")
    wordLettersChecked = 0
    for line in form:
        if(re.search(colorExp, line)):
            letter = line[57] 
            color = alphabet[letter.lower()] 
            uForm.write(("			<span style=\"background-color:{color}\" class=\"letter\">{letter}</span>\n").format(color=color, letter=letter)) 
        elif(re.search(fiveExp, line)):
            if(wordPositions[wordLettersChecked] != "_"):
                letter = line[27] 
                uForm.write(("			<span class=\"oneLetter\">{letter}</span>\n").format(letter=wordPositions[wordLettersChecked].upper()))
            else:
                uForm.write(("			<span class=\"oneLetter\">-</span>\n"))                
            wordLettersChecked += 1
        else:
            uForm.write(line)
    uForm.close()
    form.close()

# filter function for 1 word
def filterWord(word):
    accept = True
    for letter in word:
        if letter in notInWord:
            accept = False
    for letter in inWord:
        if letter not in word:
            accept = False
    for i in range(0, 5):
        if(wordPositions[i] != "_"):
            if(word[i] != wordPositions[i]):
                accept = False
    return accept

# filter through the pandas frame
def filterFrame():
    global dictionaryDF
    if("words" in dictionaryDF):
        dictionaryDF = dictionaryDF[dictionaryDF["words"].apply(filterWord)]
        if(dictionaryDF.shape[0] <= 0):
            storedDFs.append("<p>No more words left!</p>")
        else:
            storedDFs.append(dictionaryDF.to_html())
    else:
        storedDFs.append("<p>No more words left!</p>")

# converts dictionaryDF to HTML file
def showFrame(number):
    return storedDFs[number-1]

