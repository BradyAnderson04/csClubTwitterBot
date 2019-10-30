import os
# insert twitter authentication here

# or look up how to set up environment variables

# retrieve keys from environment variables
consumer_key = os.environ['TWBOT_CON_KEY']
consumer_secret = os.environ['TWBOT_CON_SECRET']
access_token = os.environ['TWBOT_ACCESS_TOKEN']
access_secret = os.environ['TWBOT_ACCESS_SECRET']
handle = os.environ['TWBOT_HANDLE']


# final steps in twitter bot
'''
1.Get api credentials
2.Set api credentials
3.Setup and test
'''