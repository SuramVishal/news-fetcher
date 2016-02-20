def getatt(url):
	f=open('att.txt','r')
	#print("hi");
	for line in f:
	    word=line.split()
	    if word[0] in url.lower():
	    	return word
def find(url):
	x=getatt(url);
	if  x!= None and len(x)>3:
		for i in range(4,len(x)):
			x[3]=x[3]+" "+x[i]
	return x	
def gettag(url):
	intag=open('rsstag.txt','r');
	k=[]
	for l1 in intag:
		k=l1.split();
		if k[0] in url.lower():
			intag.close()
			return k
		
#for i in range(0,4):
#	print x[i]
