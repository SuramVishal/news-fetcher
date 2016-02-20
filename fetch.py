import getatt
import feedparser
import time
import requests
import urllib
from bs4 import BeautifulSoup
import sys

inp=open('input.txt','r');
n=0;
url=[]
#get all url from an input file
for line in inp:
    w=line.split()
    s=str(w[0])
    url.append(s)
    n=n+1
#print(url) 
out=open('feeds.db','w');


for i in range(0,n):
	#for each rss_url get timestamp
	#then link to actual url 
	#print url[i][0]
	tag=getatt.gettag(url[i])
	feed = feedparser.parse(str(url[i]))
	date=time.strftime("%d %b %Y");
	#print(date)
	#date="30 Jan 2016"

	print(len(feed["items"]))
	for item in feed["items"]:
		#print("hi")
		
		if date in item[tag[1]].encode('ascii','ignore'):
			s=item[tag[1]].encode('ascii','ignore')
			print(s)
			out.write(s+'\n')
			#write title to the file
			print item[tag[2]]
			out.write(item[tag[2]].encode('ascii','ignore')+'\n')
			#get actual url link from feed and scarpe it
			print(item[tag[3]])
			htmlfile=urllib.urlopen(item[tag[3]])
			htmltext=htmlfile.read()
			
			soup=BeautifulSoup(htmltext)
			word=getatt.find(url[i])
			if word!=None and len(word)==2:
				g_data=soup.find_all(word[1])
			else:
				g_data=soup.find_all(word[1],{word[2]:word[3]})
		
			for item in g_data:
				out.write(item.text.encode('ascii','ignore')+"\n");
			
			#write the matter from url link to file
			
			#add delimiter at end of record
			out.write("\n-|\n")
			print
			print
	
		
