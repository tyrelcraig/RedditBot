#!/usr/bin/python

# Tyrel Craig Practice Bot.


# Import the required packages.
import praw
import pdb
import re
import os

# Choose which bot to run as named in the praw.ini file. Creates the Reddit Instance

reddit = praw.Reddit('TyrelCraigPracticeBot')

# In case the "Posts Replied To:" list doesn't exist. Create an empty List.
# Else: read in .txt and parse in list.

if not os.path.isfile("Posts_Replied_To.txt"):
	posts_replied_to = []
else:
	with open("Posts_Replied_To.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

# Choose which subreddit to run your bot in.

subreddit = reddit.subreddit("pythonforengineers")

# Choose which submission category to  run your bot in.

#category = "hot"

for submission in subreddit.hot(limit=15):
	if submission.id not in posts_replied_to:
		if re.search("i love python", submission.title, re.IGNORECASE):
			submission.reply("Tyrel Craig Practice Bot says: Test 1 Complete")
			print("Bot replying to : ", submission.title)
			posts_replied_to.append(submission.id)

with open("Posts_Replied_To.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")


