"""
Created on Mon Mar 01 1:09:00 2015

@author: Rodolfo Viana
"""

# This program ranks popular word on the file

import operator


# Count words
def count_words():
    file_in = open("tweet_label.txt", "r")
    file_out = open("words_count.txt", "w")

    dict_words_num = {}

    for tweet in file_in:
        for word in tweet.split("Text:")[1].split(" "):
            if dict_words_num.has_key(word.lower()):
                dict_words_num[word.lower()] += 1
            else:
                dict_words_num[word.lower()] = 0

    dict_words_num = sorted(dict_words_num.items(), key=operator.itemgetter(1))

    file_out.write(str(dict_words_num))

    file_in.close()
    file_out.close()

# Main
def main():
    count_words()
    pass

if __name__ == '__main__':
    main()