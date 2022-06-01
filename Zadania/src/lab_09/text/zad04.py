import snscrape.modules.twitter as sntwitter
import pandas as pd


tweets_list2 = []

for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper('#ukraina since:2022-02-02 until:2022-06-06 near:"Gdańsk", within:100km').get_items()):
    if i > 100:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])


tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df2.head(5).values)



