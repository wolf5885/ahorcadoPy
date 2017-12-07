from random import randint

def selectWordFromWordList(wordList):
	return wordList[randint(0, len(wordList) - 1)]





def masqWord(word):
	masquerade = []
	
	for i in range(len(word)):
		masquerade.append("-")
	
	return masquerade





def wordToList(word):
	return list(word)





def isLetterInWord(letter, wordAsList, maskedWordAsList):
	counter = 0
	
	for i in range(len(maskedWordAsList)):
		if word[i] == letter:
			maskedWordAsList[i] = letter
			counter += 1
	
	if counter > 0:
		return True
	else:
		return False
