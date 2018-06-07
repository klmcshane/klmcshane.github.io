from bs4 import BeautifulSoup
from urllib import request
#opens up beautifulsoup and the urllibrary
url = "http://d.lib.rochester.edu/teams/text/bowers-canterbury-tales-fifteenth-century-interlude-and-marchants-tale-of-beryn"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

#gets the file and makes it a soupy thing
table = soup.findAll('table')[0]
poem = table.findAll('tr')[0].findAll('td')[1].text
#sets variables for the stuff from the tables

print(poem)
#tells it to print everything stored in poem
f = open('beryn.txt','w')
f.write(poem)
f.close()
#puts the output into a text file
