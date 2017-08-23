import os
import subprocess

spamdir='enron1/spam'

spam_mails=os.listdir(spamdir)

ls=len(spam_mails)


dict={}
#for filename in spam_mails[0]:
newfile=open('spamdata.txt','w')

nofemails=0
for filename in spam_mails:
	email=open('enron1/spam/'+filename,'r')
	x=email.read().split()
	for words in x:
		if(words not in dict and words.isalpha() and len(words)>=4):
			dict[words]=len(subprocess.check_output('grep -il '+words+' '+spamdir+'/*.txt',shell=True).splitlines())
			pwordgivenspam=dict[words]/(ls*1.0)
			newfile.write(words+','+str(pwordgivenspam)+',')
	email.close()
	nofemails=nofemails+1;
	print(nofemails)


#print(dict['grayish'])
