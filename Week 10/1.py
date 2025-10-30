
print("Will look for the word counts:")
Sentence = input("type sentance here:")
def word_fequency(thesentence):
    wordcount = {}
    words = thesentence.lower().split()
    for word in words:
        wordcount[word] = wordcount.get(word, 0) + 1
    return wordcount
 #dictanary  
yes = word_fequency(Sentence)
print(f"{yes}")