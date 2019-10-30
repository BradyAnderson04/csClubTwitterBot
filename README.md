# Halloween Costume Bot!
This bot will tell you what you should be for Halloween! I came up with this idea when one of my friends was struggling with something to choose for Halloween. 

The technology being used in this bot is what helps keep it relevant. My bot will scan the internet for 5 different recent articles. From there it will use natural language processing via the NLTK python library to data mine the 3 most common Proper Nouns written in each article. From there it will assign a random 'modifyer' (adjective) and a random proper noun! 

To use, simple tweet
@twitterHandle What should I be for Halloween? 

Due to time constraint I did not elect to process the tweet and only respond to that, and the proper noun generation isn't perfect since I couldn't fully train my algorithm to perfection. However, I would say this is a reliable decision maker when in comes to spooky szn!

## Setup
1. Clone this repository or just copy the code from `bot.py`
1. Run `pip install -r requirements.txt` to install dependencies
1. Modify the code to your liking
1. To run the bot, just run `python bot.py`
