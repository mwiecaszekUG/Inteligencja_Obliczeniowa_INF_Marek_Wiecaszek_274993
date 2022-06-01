from nltk.tokenize import word_tokenize
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
import matplotlib.pyplot as plt


nltk.download(['punkt', 'stopwords', 'wordnet', 'omw-1.4'])

file = open("article.txt", "r")
text = ""

for line in file:
    text = text + line

tokenized_word = word_tokenize(text.lower())
print(tokenized_word)
print("Ilość słów: ", len(tokenized_word))

stop_words = list(nltk.corpus.stopwords.words('english'))
inter = [".", ",", "!", "?", "-", "_", "...", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "-", "/", "[", "]",
         "{", "}", "`", "'", "\"", "``", "''", "c't", "ca", "'s", "'re", "we", "He", 'he', "She", "she", "The", "the"]

for s in inter:
    stop_words.append(s)

filtered_words = list(filter(lambda word: word not in stop_words, tokenized_word))

print(filtered_words)
print("Ilość słów: ", len(filtered_words))

lem = WordNetLemmatizer()

leminazed = []

for word in filtered_words:
    leminazed.append(lem.lemmatize(word, "v"))

print(leminazed)
print("Ilośc leminazied: ", len(leminazed))



# tokenizer to remove unwanted elements from out data like symbols and numbers
words = ""
for w in leminazed:
    words += w + " "

words = nltk.word_tokenize(words)
fd = nltk.FreqDist(words)

print(fd.tabulate(10))

from wordcloud import WordCloud

wordcloud = WordCloud(max_font_size=25, max_words=50, background_color="white").generate(' '.join(list(words)))
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()



