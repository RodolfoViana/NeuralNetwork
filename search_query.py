"""
Created on Mon Feb 03 20:10:35 2014

@author: Rodolfo
"""
import twitter
import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")

myApi=twitter.Api(consumer_key='Q6KsZDoY5vNUAyeQhY1Xaw', consumer_secret='mvO4XXnPz2KLvPD6KR5N2S19a1CTiHkN8PKZRv1KQ', access_token_key='44794860-ShHgE1f3MI6TqJ5cyJt7DWTzQ8vVxjbaWC5MMGZSy',  access_token_secret='i2r27D09rJiwn4wNs1QBe0uRmsMTor2SzK0iV8e9AD006')

def search_query():
#    query = '(mcdonalds OR Mcdonalds) AND (happy OR sad)' # Query for mcdonalds

    geo = ('40.76222', '-73.9844', '15mi') # Times Square (NYC)
    query = 'apple'
    
    
    MAX_ID = None
    tweets = []
    K = 18
    for it in range(K): # Retrieve up to K * 100 tweets
        temp_tweets = [json.loads(str(raw_tweet)) for raw_tweet \
                in myApi.GetSearch(query, geo, count = 100,
                    max_id = MAX_ID)]#, result_type='recent')]

        tweets = tweets + temp_tweets
        print('Tweets retrieved: %d' % len(tweets))
        if temp_tweets:
            MAX_ID = temp_tweets[-1]['id']
            
    file_out = open('DataTweet.txt','a+')
    
    for raw_tweet in tweets:
        file_out.write('ID: ' + str(raw_tweet['id']) + ' -- ' + 'Text: ' + raw_tweet['text'] + '\n' )
        
    file_out.close()


def main():
    search_query()
    pass

if __name__ == '__main__':
    main()
