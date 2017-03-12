import praw       # Reddit API
import config     # Imports my config file
import time       # Allows the bot to sleep zzzzzzzzzzzzzzzzzzzzzz
import os         # Allows the script to communicate with the operating system. This is so i can store the comment id's
import sys        # Allow traceback


#Logs in the bot with the information from the config file and prints in console that is was successful
def bot_login():
	print("Attempting to log in...")
	#login with praw
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Rick roll comment responder v0.1")
	print("login was succesful!")
	
	return r
	


def run_bot(r, comments_replied_to):
	print("getting the latest 500 comments...")

	#fetches the last 500 comments in the pointed to subreddit
	for comment in r.subreddit('test').comments(limit = 500):
		    #if the link for Never Gunna Give you up is found, a reply is printed
			if "https://www.youtube.com/watch?v=dQw4w9WgXcQ" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
				print ("Rick Roll Found!") and comment.id
				comment.reply(" This link is a Rick Roll! [Here](https://www.youtube.com/watch?v=dQw4w9WgXcQ) is the correct link")
				print("replied to comment") and comment.id
			
				comments_replied_to.append(comment.id)
				#opens a file used to store comment id's
				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")
			elif "http://imgur.com/gallery/R390EId" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
				print ("Peyton Manning!") and comment.id
				comment.reply(" This link is a picture of Peyton Manning in a black mask! [Here](http://imgur.com/gallery/R390EId) is the correct link")
				print("replied to comment") and comment.id
			
				comments_replied_to.append(comment.id)
				#opens a file used to store comment id's
				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")		
def remove_comment():	
	#removes downvoted comments
	for comment in r.user.me().comments.new(limit=25):
		if comment.score < -2:
			comment.delete()
			print( "score too low, comment removed:"  + str(comment) + '\n')
			formattedmessage = 'score too low, comment removed:'  + str(comment) + '\n'
			r.user.me().message(recipient=username, subject='Comment Removed', message=formattedmessage)
			print(formattedmessage)
			print("comment delete")
			
	
	#makes the bot go to sleep when it is done writing comments
	print("going to go sleep for 30 minutes")
	#sleep for 30 minutes
	time.sleep(1800)


# makes sure the comments werent replied to earlier
def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))

	return comments_replied_to


	
r = bot_login()
comments_replied_to = get_saved_comments()
print (comments_replied_to)

while True:
	run_bot(r, comments_replied_to) 
	remove_comment()

	