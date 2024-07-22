import json
from twitter.scraper import Scraper

# Sign in with your email, username, & password 
email = ""
username = ""
password = ""

# Initialize the scraper
scraper = Scraper(email, username, password)

# Get followers for a given user ID, you can find someone's userID through this: 
#https://ilo.so/twitter-id/ 
# Integer input btw 
user_id = []
followers = scraper.followers(user_id)