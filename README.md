# dictionaryFilterWebApp
This is a tool inspired off my love for Wordle (though I have no association with the official game). Simply launch the web app, pop open Wordle side-by-side, enter guesses into Wordle, and report the outcomes (correct and incorrect letters and their positions) in the app. The program will print out possible candidate words after each guess.

Enjoy!

Note: This program uses a dictionary obtained from https://github.com/dwyl/english-words . Specifically, I duplicated the "words_alpha.txt" file from that repo. I then extracted all of the 5-letter words into a text file called "fiveLetterWords.txt" and added an extra row at the top to serve as one of the column's titles in the dataframe.