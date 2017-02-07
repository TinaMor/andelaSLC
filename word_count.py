#import re

def words(n):

	#n = n.lower()

	#n = re.sub(r'\s', ' ', n) #Matches Unicode whitespace characters (which includes [ \t\n\r\f\v]
	n = " ".join(n.split()) # Remove any excess whitespaces

	sentence = n.split(" ")
	wordsList = set(sentence)

	result = {}

	for w in wordsList:

		counter = []
		if w.isnumeric() == True:
			w = int(w)

		for idx, word in enumerate(sentence):
			if word.isnumeric() == True:
				word = int(word)

			if word == w:
				counter.append(idx)


		result[w] = (len(counter))

	print (result)