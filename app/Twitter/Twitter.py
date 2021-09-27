"""
Python class that provides all twitter core functions
"""

import tweepy


class Twitter:

    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, TOKEN_SECRET):

        # Init credentials
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)

        # Create twitter bot object
        self.__bot = tweepy.API(auth)

    def get_home_timeline_tweets(self, count=20):
        """
        Get home timeline.
        count : Number of tweets to render
        return : Twitter's response in json
        """
        return self.__bot.home_timeline(count=count)

    def get_user_timeline_tweets(self, screen_name="EmmanuelMacron", count=20):
        """
        Get specific user home timeline
        count : Number of tweets to render
        screen_name : Screen name of user to get timeline
        return : Twitter's response in json
        """
        return self.__bot.user_timeline(screen_name=screen_name, count=count)

    def tweet(self, text):
        """
        Tweet on home timeline.
        text : The text to be tweeted
        return : Status object
        """
        tweets = self.__bot.update_status(text)

        return tweets

    def _upload_media(self, media_path):
        """
        Upload media to twitter
        """
        pass

    def search(self, q, lang="fr", count=20):
        """
        Search tweets depending on criteria
        return : List of status object
        """
        return self.__bot.search(q=q, lang=lang, count=count, tweet_mode='extended')
