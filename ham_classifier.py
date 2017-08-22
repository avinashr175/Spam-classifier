import os
import subprocess

hamdir='enron1/ham'

ham_mails=os.listdir(hamdir)

lh=len(ham_mails)


dict={}
#for filename in spam_mails[0]:
newfile=open('hamdata.txt','w')

nofemails=0
for filename in ham_mails:
	email=open('enron1/ham/'+filename,'r')
	x=email.read().split()
	for words in x:
		if(words not in dict and words.isalpha() and len(words)>=4):
			dict[words]=len(subprocess.check_output('grep -il '+words+' '+hamdir+'/*.txt',shell=True).splitlines())
			pwordgivenham=dict[words]/(lh*1.0)
			newfile.write(words+','+str(pwordgivenham)+',')
	email.close()
	nofemails=nofemails+1;
	print(nofemails)


#print(dict['grayish'])
