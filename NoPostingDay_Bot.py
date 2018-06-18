import time
import praw
import Config

r = praw.Reddit(user_agent=Config.USER_AGENT,
	username=Config.USERNAME, password=Config.PASSWORD,
	client_id=Config.CLIENT_ID, client_secret=Config.CLIENT_SECRET,
	refresh_token=Config.REFRESH_TOKEN)

reply = Config.MESSAGE
reply += "\n\n----------\n\n"
reply += Config.SIGNATURE

while True:
    for post in r.subreddit('me_irl').stream.submissions():
        if post.created > Config.START_DATE:
            try:
                post.reply(reply)
            except praw.exceptions.APIException:
                print("APIException occurred")
