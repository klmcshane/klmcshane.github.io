import nltk
#import opens up and loads a package for the active file


def open_file_and_get_text(filename):
    #gives filename, opens it
    with open(filename, 'r') as our_file:
        #takes the file and reads the text, and stores it
        #you could open them a bunch at a time in two operations
        text = our_file.read()
    return text

def clean_tokens(tokens):
    #given some tokens, lowercase them all
    words = nltk.word_tokenize(text)
    clean_words =[]
    #make a loop to run all the things in words
    for word in tokens:
        #add the lowercased version of words to the list clean_words
        clean_words.append(word.lower())
    return clean_words

our_file = "eyre.txt"
# I think we are getting it to scrape and read

text = open_file_and_get_text(our_file)
words = nltk.word_tokenize(text)
clean_words = clean_tokens(words)

#print the first 30 words of the clean list
print(clean_words[0:30])
word_counts = nltk.FreqDist(clean_words)
print(word_counts['love'])
nltk.Text(clean_words).dispersion_plot(["jane", "love", "tony"])
