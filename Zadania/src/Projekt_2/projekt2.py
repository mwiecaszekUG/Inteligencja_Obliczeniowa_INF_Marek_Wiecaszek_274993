import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.stem.wordnet import WordNetLemmatizer
import numpy as np

# porównanie #justiceforjhonny vs #amberturd (nowe tweety) || #jhonnydepp vs #amberheard (z przed paru lat)

stop_words = list(nltk.corpus.stopwords.words('english'))
inter = [".", ",", "!", "?", "-", "_", "...", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "-", "/", "[", "]", "{",
         "}", "`", "'", "\"", "``", "''", "c't", "n't", "ca", "'s", "'re", "we", "He", 'he', "She", "she", "The", "the",
         "johnny", "depp", "amber", "heard", "https", "t", "co", "johnnydepp", "u", "m", "amberheard", "t co", ":"
                                                                                                               "johnnydepp t",
         "t.co", "&amp", "amp", "'m", "#johnnydepp", "#amberheard", "one"]

for s in inter:
    stop_words.append(s)


def getTweets(query, list, amount):
    for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(query).get_items()):
        if i > amount:
            break
        list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])


def getTimeFrame(monthSince, yearSince, monthUntil, yearUnitl, hashtag, amPerMonth):
    allTweets = []

    while yearSince <= yearUnitl:
        if yearSince == yearUnitl and monthUntil == monthSince:
            break
        monthlyTweets = [f'{yearSince}-{monthSince}']
        print(yearSince, "-", monthSince)
        if monthSince == 12:
            for i, tweet in enumerate(
                    sntwitter.TwitterSearchScraper(
                        f'#{hashtag} lang:en since:{yearSince}-12-1 until:{yearSince + 1}-{1}-1').get_items()):
                if i > amPerMonth:
                    allTweets.append(monthlyTweets)
                    monthSince += 1
                    break
                monthlyTweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
            monthSince = 1
            yearSince += 1
        else:
            for i, tweet in enumerate(
                    sntwitter.TwitterSearchScraper(
                        f'#{hashtag} lang:en since:{yearSince}-{monthSince}-1 until:{yearSince}-{int(monthSince) + 1}-1').get_items()):
                if i > amPerMonth:
                    break
                monthlyTweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
            allTweets.append(monthlyTweets)
            monthSince += 1

    return allTweets


def makeWordCloud(dataframe):
    text = " ".join(dataframe['Text'])

    tokenized_word = nltk.tokenize.word_tokenize(text.lower())
    filtered_words = list(
        filter(lambda word: word not in stop_words and word[:2] != "//" and word != ":", tokenized_word))

    lem = WordNetLemmatizer()
    leminazed = []
    for word in filtered_words:
        leminazed.append(lem.lemmatize(word, "v"))

    words = ""
    for w in leminazed:
        words += w + " "

    words = nltk.word_tokenize(words)
    print(words)

    wordcloud = WordCloud(max_font_size=50, max_words=60, background_color="white").generate(' '.join(list(words)))
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def predict_feelings(dataframe):
    text = ". ".join(dataframe['Text'])

    sentances = nltk.tokenize.sent_tokenize(text)

    neu = 0
    pos = 0
    neg = 0
    com = 0

    for sentence in sentances:
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(sentence)
        com += ss["compound"]
        neg += ss["neg"]
        neu += ss["neu"]
        pos += ss["pos"]
    return "Compound: ", com, " Negative: ", neg, " Neutral: ", neu, " Positive: ", pos


def predict_on_timeframe(dataframe):
    text = ". ".join(dataframe['Text'])
    sentances = nltk.tokenize.sent_tokenize(text)
    com = 0

    for sentence in sentances:
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(sentence)
        com += ss["compound"]
    return com


# jdOld = []
#
# getTweets('#johnnydepp lang:en until:2016-05-05', jdOld, 15000)
#
# tweets_jdOld = pd.DataFrame(jdOld, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
#
# print(tweets_jdOld.head(5).values)
# print(len(tweets_jdOld))
#
# tweets_jdOld.to_csv("oldJhonny.csv")
#
# ahOld = []
#
#
# getTweets('Amber Heard lang:en until:2016-05-05', ahOld, 7500)
# getTweets('#amberheard lang:en until:2016-05-05', ahOld, 7500)
#
# tweets_ahOld = pd.DataFrame(ahOld, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
#
# print(tweets_ahOld.head(100).values)
# print(len(tweets_ahOld))
#
# tweets_ahOld.to_csv("OldAmber.csv")

# ahNew = []
#
# getTweets('#amberheard lang:en since:2022-05-05', ahNew, 15000)
#
#
# tweets_ahNew = pd.DataFrame(ahNew, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
#
# print(tweets_ahNew.head(100).values)
# print(len(tweets_ahNew))
#
# tweets_ahNew.to_csv("NewAmber.csv")
#
# jdNew = []
#
# getTweets('#johnnydepp lang:en since:2022-05-05', jdNew, 15000)
#
#
# tweets_jdNew = pd.DataFrame(jdNew, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
#
# print(tweets_jdNew.head(100).values)
# print(len(tweets_jdNew))
#
# tweets_jdNew.to_csv("NewJhonny.csv")

# OldJhonny = pd.read_csv("oldJhonny.csv")
# NewJhonny = pd.read_csv("NewJhonny.csv")
# OldAmber = pd.read_csv("OldAmber.csv")
# NewAmber = pd.read_csv("NewAmber.csv")
#
# makeWordCloud(OldJhonny)
# makeWordCloud(NewJhonny)
# makeWordCloud(OldAmber)
# makeWordCloud(NewAmber)

# predyckja opinni

# pred_1 = predict_feelings(OldJhonny)
# pred_2 = predict_feelings(NewJhonny)
# pred_3 = predict_feelings(OldAmber)
# pred_4 = predict_feelings(NewAmber)
#
# print("Preykcja dla starych tweetów o Johnnym: ", pred_1)
# print("Preykcja dla nowych tweetów o Johnnym: ", pred_2)
# print("Preykcja dla starych tweetów o Amber: ", pred_3)
# print("Preykcja dla nowych tweetów o Amber: ", pred_4)


# porównanie po miesiącach 2016-czerwiec do 2022-czerwiec


johhny_timeframe = getTimeFrame(6, 2016, 6, 2022, "#johnnydepp", 250)

johhny_tweets = []

for i in range(len(johhny_timeframe) - 1):
    to_add = pd.DataFrame(johhny_timeframe[i + 1][1:], columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    johhny_tweets.append(to_add)

amber_timeframe = getTimeFrame(6, 2016, 6, 2022, "#amberheard", 250)


amber_tweets = []

for i in range(len(amber_timeframe) - 1):
    to_add = pd.DataFrame(amber_timeframe[i + 1][1:], columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    amber_tweets.append(to_add)

johnny_results = []
#[39.95109999999998, 28.9384, 17.534399999999994, 69.62969999999994, 64.43439999999998, 62.31139999999994, 48.57229999999997, 53.87189999999995, 28.899600000000003, 51.606299999999976, 36.29649999999999, 33.91279999999998, 74.67159999999997, 50.786300000000026, 49.28779999999996, 39.758199999999974, 24.491499999999988, 49.53539999999995, 75.87929999999997, 55.337799999999966, 83.61899999999999, 74.68400000000004, 54.59999999999996, 59.45039999999991, 58.98419999999992, 68.0248, 71.90739999999998, 42.282199999999996, 74.95330000000003, 122.67269999999999, 56.46719999999997, 70.81029999999998, 14.202100000000014, 63.415899999999965, 14.63470000000001, 60.48379999999996, 70.73309999999992, 34.48000000000003, 61.28819999999997, 48.88439999999998, 28.78129999999999, 72.2166, 26.80419999999999, 17.586399999999994, 23.988799999999998, 14.742799999999994, 53.458099999999966, 18.548299999999994, 30.69490000000002, 18.857399999999977, 54.96479999999997, 62.897699999999915, 61.64729999999997, 111.39069999999998, 40.41489999999996, 24.700300000000006, 31.85600000000001, 32.505600000000015, 29.89330000000001, 24.751600000000007, 13.37160000000001, 84.5307999999999, 62.18199999999998, 53.97910000000001, 52.31739999999993, 62.59359999999994, 59.539199999999965, 7.122900000000001, 1.3239999999999963, 3.361800000000007, 22.23539999999998]
amber_results = []

for month in johhny_tweets:
    johnny_results.append(predict_on_timeframe(month))

print(amber_results)

for month in amber_tweets:
    amber_results.append(predict_on_timeframe(month))

plt.title("Porównanie po miesiącach")
plt.xlabel("Upływ czasu(kolejne miesiące")
plt.ylabel("Wynik predykcji")
plt.plot(np.array(johnny_results), color="blue")
plt.plot(np.array(amber_results), color="red")
plt.legend(["Jhonny", "Amber"])
plt.show()
