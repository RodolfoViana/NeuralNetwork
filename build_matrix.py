"""
Created on Mon Mar 01 20:23:20 2015

@author: Rodolfo Viana
"""

# This program build one matrix, with number of time that each tweet has some words (most popular words) and label

def build_matrix():
    file_in = open("tweet_label.txt", "r")

    count = 0
    for line in file_in:
        if (not line.split(",")[-1][0].__eq__("2")) and (not line.split(",")[-1][0].__eq__("1")):
           print line
    print count

# Main
def main():
    build_matrix()
    pass

if __name__ == '__main__':
    main()