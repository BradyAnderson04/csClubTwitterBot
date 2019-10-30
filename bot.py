import tweepy
from datetime import datetime
import random
from secret import consumer_key, consumer_secret, access_token, access_secret, handle
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
from nltk import ne_chunk
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from bs4 import BeautifulSoup
import html5lib
import requests
import re
import nltkArticle
nlp = en_core_web_sm.load()

# get authentication info
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret) 

# log into the API
api = tweepy.API(auth)
print('[{}] Logged into Twitter API as @{}\n-----------'.format(
    datetime.now().strftime("%H:%M:%S %Y-%m-%d"),
    handle
))

# string array of words that will trigger the on_status function
trigger_words = [
    '@' + handle # respond to @mentions
]

# set up proper name gathering based off the 4 different articles
articleList = ['https://www.forbes.com/sites/danidiplacido/2019/03/31/what-i-dont-understand-about-pewdiepie/#4b036fab42d5','https://www.nationalreview.com/corner/who-is-the-democratic-frontrunner/', 'https://www.gamesradar.com/rick-and-morty-season-4-release-date-cast-trailer-new-episodes/', 'https://www.theguardian.com/technology/2019/oct/23/google-claims-it-has-achieved-quantum-supremacy-but-ibm-disagrees' ]
propNoun = []
for i in articleList:
    articleURL = nltkArticle.url_to_string(i)
    article = nltkArticle.nlp(articleURL)
    items = [x.text for x in article.ents]
    propNoun.append(Counter(items).most_common(5))
    print(Counter(items).most_common(3))
print(modifiers, propNoun)

modifiers = [
    'sexy',
    'goofy',
    'emotionally unsatisfied',
    'spooky',
    'edgy',
    'angsty',
    'epic',
    'sleepy',
    'hungry',
    'illeagal'
    'scary',
    'anti-social'
]

# override the default listener to add code to on_status
class MyStreamListener(tweepy.StreamListener):

    # listener for tweets
    # -------------------
    # this function will be called any time a tweet comes in
    # that contains words from the array created above
    def on_status(self, status):

        # log the incoming tweet
        print('[{}] Received: "{}" from @{}'.format(
            datetime.now().strftime("%H:%M:%S %Y-%m-%d"),
            status.text,
            status.author.screen_name
        ))

        # get the text from the tweet mentioning the bot.
        # for this bot, we won't need this since it doesn't process the tweet.
        # but if your bot does, then you'll want to use this
        message = status.text

        # after processing the input, you can build your output
        # into this variable. again, since we're just reply "No.",
        # we'll just set it as that.

        # get a random halloween costume
        adjective = modifiers[random.randint(0, len(modifiers))]
        halloweenObject = propNoun[random.randint(0,len(propNoun))]

        # response
        response = 'You should be a', adjective, halloweenObject,'!'
        print(response)

        # respond to the tweet
        api.update_status(
            status=response,
            in_reply_to_status_id=status.id
        )

        print('[{}] Responded to @{}'.format(
            datetime.now().strftime("%H:%M:%S %Y-%m-%d"),
            status.author.screen_name
        ))

# create a stream to receive tweets
try:
    streamListener = MyStreamListener()
    stream = tweepy.Stream(auth = api.auth, listener=streamListener)
    stream.filter(track=trigger_words)
except KeyboardInterrupt:
    print('\nGoodbye')