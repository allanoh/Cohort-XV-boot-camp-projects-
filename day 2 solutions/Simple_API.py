from twython import Twython, TwythonError# Importing the twython module and the twython error handling module to be used in the API

#Authentication keys gotten from the twitter developer profile
	app_key = "GBQnPh2kzgU8GAMXSTVaWyUhH"
	app_secret = "ki1a8TwT6mGkyqZvJozwefbLN0Mwwarg2sBXbcZRXkgYPVuuri"
	token = "99288635-vn1jYgxQsttU3O4jXqUtmQLztMOdR1RWRBGAZgq29"
	auth_secret = "Cq1NwIkjJ4FeiktJVX93bsfxzXQxEHkB1Jz82wlM17biR"


twitter = Twython(app_key, app_secret, token, auth_secret)

#Sending a tweet via the API
twitter.update_status(status="Finally done with the API,flooding your timeline in a jiffy,lol")

# retweeting tweets automatically based on the query given.
search_results = twitter.search(q="#TogwamuSuubi", count=20)
# implementing a try-except block to handle errors arising in the search query
try:
    for tweet in search_results["statuses"]:
        try:
            twitter.retweet(id = tweet["id_str"])
        except TwythonError as e:
            print e
except TwythonError as e:
    print e