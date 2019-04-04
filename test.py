import random
import numpy as np
import os

with open('wordlengthprobs.txt',"r") as file:
	wlps = file.read().split(', ')

wordlengths = []
lengthprobs = []

for wlp in wlps:
	w = wlp.split(': ')
	if w[0] > 0:
		wordlengths.append(int(w[0]))
		lengthprobs.append(float(w[1]))

lengthprobs = np.array(lengthprobs)
lengthprobs /= lengthprobs.sum()

with open('letters40000.txt',"r") as file:
	letters = file.read().split('\n')
	letters.pop()

justletters=[]
justprob=[]

for letter in letters:
	l=letter.split(' \t')
	justletters.append(str(l[0]))
	justprob.append(float(l[1]))

justprob = np.array(justprob)
justprob /= justprob.sum()

sentlengths = range(3,21,1)#[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sentprobs = [1.0/len(sentlengths)]*len(sentlengths) #[1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18,1.0/18]

numsentences = 10 #later should add a thing to vary this
paragraph = ''

for n in range(numsentences):
	sentence = ''
	sentencelength = np.random.choice(sentlengths,1,p=sentprobs,replace=1)

	for i in range(sentencelength):
		wordlen = np.random.choice(wordlengths,1,p=lengthprobs,replace=1)
		word = ''

		for i in range(wordlen):
			result = np.random.choice(justletters,wordlen,p=justprob,replace=1)

		for r in result:
			word += str(r)
		sentence = sentence+word.lower()+' '

	firstletter = sentence[0].upper()
	sentence = sentence[1:-1] #gets rid of first letter and last space before punctuation
	sentence = firstletter+sentence+'.'

	paragraph = paragraph+sentence+' '

paragraph = '\t'+paragraph

print paragraph

f = open('output.txt','w')
f.write(paragraph)
f.close()
