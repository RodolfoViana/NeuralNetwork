"""
Created on Mon Mar 01 19:01:23 2015

@author: Rodolfo Viana
"""

# This program label tweet as negative or not negative

def label_tweet():
    file_in = open("data_tweet.txt", "r")
    file_out = open("tweet_label.txt", "a")

    for line in file_in:
        label = raw_input(line.split("Text:")[1] + ": ")
        file_out.write(line + "," + label + "\n")


    file_in.close()
    file_out.close()

def main():
    label_tweet()
    pass


if __name__ == '__main__':
    main()