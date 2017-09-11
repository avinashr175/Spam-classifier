import os
import pwordgiven
import time

spamdir='enron1/spam'  #training dataset
hamdir='enron1/ham'

spam_mails=os.listdir(spamdir)
ham_mails=os.listdir(hamdir)

pos=(len(spam_mails)*1.0)/(len(spam_mails)+len(ham_mails))
poh=1-pos
print(pos,poh)

spamdir='enron2/spam'   #testing dataset
hamdir='enron2/ham'

spam_mails=os.listdir(spamdir)
ham_mails=os.listdir(hamdir)

correct=0
incorrect=0

t1=time.time()
for i in range(len(spam_mails)):
	testmail=spamdir+'/'+spam_mails[i];
	f=open(testmail,'r')
	data=f.read().split()
	spam=1.0
	ham=1.0
	for words in data:
			if(words.isalpha() and len(words)>=4):
				spam=spam*pwordgiven.spam(words)
				ham=ham*pwordgiven.ham(words)
	spam=spam*pos
	ham=ham*poh
	if(spam>ham):
		correct=correct+1

	else:
		incorrect=incorrect+1
	f.close()
	print(i)
t2=time.time()
print("Total time taken: %f"%(t2-t1))
print((correct*1.0)/(correct+incorrect))    # accuracy of the algo on the training dataset
