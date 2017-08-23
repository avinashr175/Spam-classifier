def ham(word):
	filename='hamdata.txt'
	f=open(filename,'r')

	data=f.read().split(',')
	count=0;
	for words in data:
		if(word==words):
			return(float(data[count+1]))
		count=count+1

	return 2.0/count

def spam(word):
	filename='spamdata.txt'
	f=open(filename,'r')

	data=f.read().split(',')
	count=0;
	for words in data:
		if(word==words):
			return(float(data[count+1]))
		count=count+1

	return 2.0/count