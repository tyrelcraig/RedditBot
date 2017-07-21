#!/usr/bin/python

# Tyrel Craig Practice Bot.


# Import the required packages.
import praw

# Choose which bot to run as named in the praw.ini file.

reddit = praw.Reddit('TyrelCraigPracticeBot')

# Choose which subreddit to run your bot in.

subreddit = reddit.subreddit("learnpython")

# Choose which submission category to  run your bot in.

#category = "hot"

# Run through the top 5 submissions and report the following information.

for submission in subreddit.hot(limit=5):
	print ("Title: ", submission.title)
	#print ("Text: ", submission.selftext)
	print ("Score: ", submission.score)
	print("-------------------- \n")