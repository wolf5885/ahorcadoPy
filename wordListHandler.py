from json import dump
from json import loads
from os import system

def populateWordList(wordList):
	system("clear")

	while True:
		word = input("Ingrese una palabra (vacia para terminar): ")

		if len(word) == 0:
			break

		word = word.upper()

		existsWordInWordList = False

		for wordTmp in wordList:
			if wordTmp == word:
				existsWordInWordList = True

		if not existsWordInWordList:
			wordList.append(word)


def saveData(wordList):
	with open("wordList.json", "w") as fileOut:
		dump(wordList, fileOut)


def loadData():
	return loads(open("wordList.json").read())
