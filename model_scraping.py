from bs4 import BeautifulSoup
#opens up beautifulsoup
html_file = open('lyric.html')
soup = BeautifulSoup(html_file, 'lxml')
#gets the file and makes it a soupy thing
table = soup.findAll('table')[0]
poem = table.findAll('tr')[0].findAll('td')[1].text
#sets variables for the stuff from the tables

print(poem)





#makes a loop telling it to produce the items in the list - I think
