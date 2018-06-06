import nltk
#import opens up and loads a package for the active file

filename = "eyre.txt"
# I think we are getting it to scrape and read
#gives filename, opens it
with open(filename, 'r') as our_file:
    #takes the file and reads the text, and stores it
    #you could open them a bunch at a time in two operations
    text = our_file.read()
#produces the first part of the text... 99 chars
print(text[0:100])
#now you're going to make it give you words/do the reading
words = nltk.word_tokenize(text)
print(words[0:10])

if "The" != "the":
    print("Does case matter?")
#Yes case matters and usually you make it lowercase, like below
clean_words =[]
for word in words:
    clean_words.append(word.lower())
print(clean_words[0:30])
