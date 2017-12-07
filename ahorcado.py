#!/usr/bin/env python3

from playGame import *

wordList = ["AMAR", "TEMER", "PARTIR", "JUGAR", "CORRER", "DORMIR"]

word = selectWordFromWordList(wordList)
wordAsList = wordToList(word)
maskedWordAsList = masqWord(word)

print(word)
print(wordAsList)
print(maskedWordAsList)

isLetterInWord("A", wordAsList, maskedWordAsList)
print(maskedWordAsList)
