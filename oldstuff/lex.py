import csv
import json 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
from bs4 import BeautifulSoup


nltk.download('vader_lexicon')
sentiment = []
word = []

with open("ratedTxt.csv", 'r', newline="") as f:
    data = csv.reader(f, delimiter=",")
    for row in data:
        sentiment.append(row[1])
        word.append(row[0])


mydict = dict(zip(word, sentiment))


myAnal = SentimentIntensityAnalyzer()
myAnal.lexicon.update(mydict)

webpage = requests.get("https://www.cnn.com/2020/05/03/investing/stocks-week-ahead/index.html")


print("done")
soup = BeautifulSoup(webpage.text, 'html.parser')

# shittext = soup.find_all(["a", 'span'])
# for shit in shittext:
#     shit.decompose()
bodytext = soup.findAll("div", {"class": "zn-body__paragraph"})


# print(bodytext)
for para in bodytext:
    print(para.text)
# zn-body__paragraph speakable
# print(webpage.text)
# print(myAnal.lexicon)

