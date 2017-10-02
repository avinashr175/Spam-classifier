import os
import pwordgiven
import time

spamdir='enron1/spam'
hamdir='enron1/ham'

spam_mails=os.listdir(spamdir)
ham_mails=os.listdir(hamdir)

pos=(len(spam_mails)*1.0)/(len(spam_mails)+len(ham_mails))
poh=1-pos



testmail='testmail.txt';
f=open(testmail,'r')
data=f.read().split()
spam=1.0
ham=1.0
for words in data:
		if(words.isalpha() and len(words)>=3):
			spam=spam*pwordgiven.spam(words)
			ham=ham*pwordgiven.ham(words)
spam=spam*pos
ham=ham*poh
if(spam<ham):
	print("This a ham (non-spam) mail.")

else:
	print("This a spam mail.")
f.close()

