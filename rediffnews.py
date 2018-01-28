import requests
from bs4 import BeautifulSoup
s1=raw_input("Enter the date in DD/MM/YYYY\n")
s3=""
for i in s1:
	if i!='/':
		s3=s3+i
s3=s3[:4]+s3[6:]
s2='http://www.rediff.com/issues/'
s2=s2+s3
s2=s2+'hl.html'
quote_page=s2
page=requests.get(quote_page)
soup=BeautifulSoup(page.content,'html.parser')
news=soup.find_all('div',id='hdtab1',)
print "Printing Headlines of",s1
s=""
x=0
ans=""
for i in news:
	s=s+i.text
for i in s:
	if i=='L':
		x=1
	if x==1:
		ans=ans+i
x=0
for i in news:
	local=i.find_all('b')
	j=0
	while x<1:
		print "1 ",local[j].text
		x=x+1
		ans=ans[(len(local[j].text)):]
		j=j+1
x=2
y=1
i=0
string=""
length=len(ans)
while i<length:
	if y==1:
		string=str(x)+" "
		x=x+1
		y=0
	string=string+ans[i]
	if ans[i]=='T' and i>=1 and ans[i-1]=='S' and i>=2 and ans[i-2]=='I':
		print string
		string=""
		y=1
	i=i+1
