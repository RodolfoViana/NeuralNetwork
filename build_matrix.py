"""
Created on Mon Mar 01 20:23:20 2015

@author: Rodolfo Viana
"""

# This program build one matrix, with number of time that each tweet has some words (most popular words) and label

def build_matrix():
    file_in = open("tweet_label.txt", "r")
    file_words = open("popular_words_w_frequency.txt", "r")

    file_out = open("matrix_tweet.txt", "w")

    popular_words = []

    for line in file_words:
        popular_words = popular_words + [line.split("'")[1]]

    dict_matrix = {}
    count = 0
    for line in file_in:
        temp = []
        for words in line.split("Text:")[1].split():
            for popular in popular_words:
                if popular.__eq__(words.lower()):
                    temp = temp + [1]
                    file_out.write("1, ")
                else:
                    temp = temp + [0]
                    file_out.write("0, ")
        temp = temp + [line.split(",")[-1]]
        dict_matrix[count] = temp
        count += 1

    file_in.close()
    file_out.close()
    file_words.close()


# Main
def main():
    build_matrix()
    pass

if __name__ == '__main__':
    main()