# Reddit_bot
A Reddit bot that detects rick rolls and notifies the users
Reddit bot for detecting rick rolls

A reddit bot that detects rick rolls and warns users about it! This is the first bot that I have made. I created it to practice python (3.x) as well as get somewhat familiar with api's (praw) as well.

Its Function

A common internet practice that has been around for a very long time is the rick roll. What happens is someone asks for a link to something and they are given the link to a youtube video. This video is Never gunna give you up by Rick Astley. Great video and great song. I think? Well regardless if you like it or not(do you really) it happens all the time.

While funny usually, I thought it would be a good idea to warn some people browsing reddit that a rick roll has appeared in the comments.

How this all goes down and functions

The bot uses some functions from PRAW to look through comments and see if the link to the song shows up every 30 minutes. It will keep running and running unless it is stopped manually.

The bot will also store the id's of who it has replied to in order to eliminate double replies or self replies. These are stored in a text file.

The bot will check its previous comments right before it goes to sleep and will delete any comments when the score reaches a certain threshold.

The authentication file is empty and is ready for the information for your bot to be put into each field.
