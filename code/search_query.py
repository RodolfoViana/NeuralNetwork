"""
Created on Mon Feb 23 20:10:35 2015

@author: Rodolfo Viana
"""

# In this program it is possible search for tweets that say anything (bad or not bad) about Apple at Times Square.

import twitter
import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")

# Load twitter api with consumer key and access token
myApi = twitter.Api(consumer_key='Q6KsZDoY5vNUAyeQhY1Xaw', consumer_secret='mvO4XXnPz2KLvPD6KR5N2S19a1CTiHkN8PKZRv1KQ',
                    access_token_key='44794860-ShHgE1f3MI6TqJ5cyJt7DWTzQ8vVxjbaWC5MMGZSy',
                    access_token_secret='i2r27D09rJiwn4wNs1QBe0uRmsMTor2SzK0iV8e9AD006')


# Search for anything related to Apple at Times Square
def search_query(set_Tweets):
    geo = ('40.76222', '-73.9844', '15mi')  # Times Square (NYC)
    query = '(apple OR iPhone OR iWatch OR iOS)'

    max_id = None
    tweets = []
    K = 18
    x = 0
    for it in range(K):  # Retrieve up to K * 100 tweets
        temp_tweets = [json.loads(str(raw_tweet)) for raw_tweet \
                       in myApi.GetSearch(query, geo, count=100, max_id=max_id)] #result_type='recent')]

        print('Tweets retrieved: %d' % len(tweets))
        if temp_tweets:
            max_id = temp_tweets[-1]['id']

    file_id = open('id.txt', 'a+')
    file_out = open('data_tweet.txt', 'a+')

    count_new_tweets = 0
    unique_tweets = set_Tweets
    for raw_tweet in tweets:

        if unique_tweets.__contains__(str(raw_tweet['id'])):
            pass
        else:
            unique_tweets.append(str(raw_tweet['id']))
            file_out.write('Id: ' + str(raw_tweet['id']) + "," + 'Text: ' + raw_tweet['text'] + ' \n')
            file_id.write(str(raw_tweet['id']) + '\n')
            count_new_tweets += 1

    print ('%d New Tweets' % count_new_tweets)
    file_id.close()
    file_out.close()


# Read file and return all tweets ID in a list of tweets ID
def read_file(file_in):
    file_in = open(file_in, "r")

    set_tweets = []
    for line in file_in:
        set_tweets.append(str(line).split("\n")[0])

    file_in.close()
    return set_tweets


# Main
def main():
    search_query(read_file("id.txt"))
    pass


if __name__ == '__main__':
    main()
