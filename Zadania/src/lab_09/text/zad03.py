from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import nltk

nltk.download(['vader_lexicon'])

bad = "I booked through booking.com for 3 adults and 3 bedrooms, and we knew the third bedroom would be the sofa bed in" \
      " the living room which was fine. But when we arrived there was no bedding for the sofa bed and I was told I needed" \
      " to have requested the third bed to be set up via an app beforehand (which I had not been told) and for an additional" \
      " charge (which was unacceptable as we had booked for three beds). Also, after booking the flat easily through booking.com" \
      " there was then a lot of work, verifying myself through superhog, installing this app, putting down a £550 deposit hold, terms" \
      " and conditions as long as my arm… far too much hassle"

good = " The hotel was extremely nice and modern and very good for what we paid. The staff were very friendly and" \
       " helpful and they held our luggage for us with no problem as we wanted to go out in the city before we could" \
       " check in at 3. When checking in they gave us free drink vouchers as we was staying at this hotel for a birthday" \
       " which was very nice of them. The room was kept very clean and the beds were very comfy. The facilities were" \
       " very good and this hotel exceeded our expectations!"

bad_list = tokenize.sent_tokenize(bad)
good_list = tokenize.sent_tokenize(good)

bad_neu = 0
bad_pos = 0
bad_neg = 0
bad_com = 0

for sentence in bad_list:
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    bad_com += ss["compound"]
    bad_neg += ss["neg"]
    bad_neu += ss["neu"]
    bad_pos += ss["pos"]

print("Dla negatywnej opinni", "Compound: ", bad_com, " Negative: ", bad_neg, " Neutral: ", bad_neu, " Positive: ", bad_pos)


neu = 0
pos = 0
neg = 0
com = 0

for sentence in good_list:
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    com += ss["compound"]
    neg += ss["neg"]
    neu += ss["neu"]
    pos += ss["pos"]

print("Dla pozytywnej opinni", "Compound: ", com, " Negative: ", neg, " Neutral: ", neu, " Positive: ", pos)