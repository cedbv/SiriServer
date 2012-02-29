#!/usr/bin/python
# -*- coding: utf-8 -*-
# Twitter
# Par Cédric Boverie (cedbv)

# For now, use the same account for everyone.
# Pre-configured with a test account

import re
from plugin import *

try:
   import tweepy
except ImportError:
   raise NecessaryModuleNotFound("Tweepy library not found. Please install Tweepy library! e.g. sudo easy_install tweepy")


consumer_key="oOUrrc7UYBLoRjSLBIQLQ"
consumer_secret="nA5Ta9zqdN5KFbGPCZuu2CwLHH8ou43fO2gN7e83w"
access_token="507859408-sdXybfdtJTKckfJLTJVNMlTwzQ8YJZr8ObDgEYU9"
access_token_secret="HWBecAnuDTM8Lq2MEOye3H0ksUc9rSiGm5YbcW9VGBk"

class Twitter(Plugin):

    res = {
        'twitter': {
            'en-US': u".*(Twitter|tweet|twit)(.*)",
            'fr-FR': u".*(Twitter|tweeter|tweet|twit|tuiteur)(.*)",
        },
        'what_to_tweet': {
            'en-US': u"What do you want to tweet?",
            'fr-FR': u"Que voulez-vous tweeter ?",
        },
        'what_to_tweet_say': {
            'en-US': u"What do you want to tweet?",
            'fr-FR': u"Que voulez-vous twiter ?",
        },
        'success': {
            'en-US': u"I just posted \"{0}\" on Twitter.",
            'fr-FR': u"J'ai envoyé \"{0}\" sur Twitter.",
        },
        'success_say': {
            'en-US': u"I just posted \"{0}\" on Twitter.",
            'fr-FR': u"J'ai envoyé \"{0}\" sur Twitteur.",
        },
        'failure': {
            'en-US': u"Something doesn't work as expected. Try again later.",
            'fr-FR': u"Quelque chose s'est mal passé. Veuillez réessayer plus tard.",
        },
    }

    @register("fr-FR", res["twitter"]["fr-FR"])
    @register("en-US", res["twitter"]["en-US"])
    def tweet(self, speech, language, regex):

        if regex.group(2) != None:
            twitterMsg = regex.group(2).strip()
        else:
            twitterMsg = ""

        if twitterMsg == "":
            twitterMsg = self. ask(self.res["what_to_tweet"][language],self.res["what_to_tweet_say"][language])

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        try:
            api.update_status(twitterMsg)
            self.say(self.res["success"][language].format(twitterMsg),self.res["success_say"][language].format(twitterMsg))
        except:
            self.say(self.res["failure"][language])

        self.complete_request()
