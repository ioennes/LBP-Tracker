import tweepy
import time

keys = open(r"C:\Users\johnc\Documents\CP2\scraper\scrape\src\keys.txt", "r").readlines()
print(keys)

key = "XXX"
secretKey = "XXX"
token = "XXX"
secretToken = "XXX"

authenticator = tweepy.OAuthHandler(key, secretKey);
authenticator.set_access_token(token, secretToken);

api = tweepy.API(authenticator, wait_on_rate_limit=True)

def check_if_modified(path):
    fname = open(path, "r").read()
    track = fname.split()
    initial = track
    # print(fname)
    api.update_status(f"{fname}")
    while True:
        fname = open(path, "r").read()
        track = fname.split()
        if track != initial:
            if track[1] > initial[1]:
                # print(f"📈 Increase\n{fname}")
                api.update_status(f"📈 Increase\n{fname}")
            elif track[1] < initial[1]:
                # print(f"📉 Decrease\n{fname}")
                api.update_status(f"📉 Decrease\n{fname}")
                
            initial = track
        
        time.sleep(10)
                
check_if_modified(r"C:\Users\johnc\Documents\CP2\scraper\scrape\src\rate.txt")
