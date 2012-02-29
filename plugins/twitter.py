#!/usr/bin/python
# -*- coding: utf-8 -*-
# Twitter
# Par Cédric Boverie (cedbv)

# For now, use the same account for everyone.
# Pre-configured with a test account

import re
from plugin import *
import ConfigParser

try:
   import tweepy
except ImportError:
   raise NecessaryModuleNotFound("Tweepy library not found. Please install Tweepy library! e.g. sudo easy_install tweepy")

try:
    config = ConfigParser.RawConfigParser()
    config.read("plugins/twitter.conf")

    consumer_key = config.get("consumer","consumer_key")
    consumer_secret = config.get("consumer","consumer_secret")
except:
    raise ApiKeyNotFoundException("You need to configure your twitter consumer_key and consumer secret to use Twitter plugin.")

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
        'not_ready': {
            'en-US': u"You must configure your Twitter account. Here is the identifant needed by the server administrator : {0}",
            'fr-FR': u"Votre compte Twitter n'est pas configuré. Voici l'identifiant que vous devez transmettre à l'administrateur du serveur : {0}",
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

        try:
            access_token = config.get(self.assistant.accountIdentifier,"access_token")
            access_token_secret = config.get(self.assistant.accountIdentifier,"access_token_secret")
        except:
            access_token = ""
            access_token_secret = ""


        if access_token != "" and access_token_secret != "":
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)
            try:
                api.update_status(twitterMsg)
                self.say(self.res["success"][language].format(twitterMsg),self.res["success_say"][language].format(twitterMsg))
            except:
                self.say(self.res["failure"][language])
        else:
            self.say(self.res["not_ready"][language].format(self.assistant.accountIdentifier))

        self.complete_request()
