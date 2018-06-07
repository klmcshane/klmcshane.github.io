import nltk

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

our_file = "chaucer_ct.txt"

text = open_file_and_get_text(our_file)
words = nltk.word_tokenize(text)
clean_words = clean_tokens(words)

word_counts = nltk.FreqDist(clean_words)
print(word_counts["endite"])
nltk.Text(clean_words).dispersion_plot(["make", "endite", "write"])
