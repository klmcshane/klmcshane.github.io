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
    clean_words =[]
    #make a loop to run all the things in words
    for word in tokens:
        #add the lowercased version of words to the list clean_words
        clean_words.append(word.lower())
    return clean_words

def read_all(poem):
    text = open_file_and_get_text(poem)
    words = nltk.word_tokenize(text)
    clean_words = clean_tokens(words)
    word_counts = nltk.FreqDist(clean_words)
    print(word_counts["endite"])
    nltk.Text(clean_words).dispersion_plot(["make", "endite", "write"])

troilus = "corpus/chaucer_troilus.txt"
canterbury = "corpus/chaucer_ct.txt"
confessio = "corpus/gower.txt"

read_all (troilus)
read_all (canterbury)
read_all (confessio)

#filename = ["corpus/chaucer_ct.txt", "corpus/chaucer_troilus.txt"]
