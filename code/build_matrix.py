"""
Created on Mon Mar 01 20:23:20 2015

@author: Rodolfo Viana
"""

# This program build one matrix, with number of time that each tweet has some words (most popular words) and label

def build_matrix():
    file_in = open("/home/rodolfo/Projetos/NeuralNetwork/pre-processing/tweet_label.txt", "r")
    file_words = open("/home/rodolfo/Projetos/NeuralNetwork/pre-processing/popular_words_w_frequency.txt", "r")

    file_out = open("matrix_tweet.txt", "w")

    popular_words = []

    for line in file_words:
        popular_words = popular_words + [line.split("'")[1]]

    for line in file_in:

        for words in popular_words:
            if line.split("Text:")[1].lower().split().__contains__(words):
                file_out.write(str(line.split("Text:")[1].lower().split().count(words)) + ",")
            else:
                file_out.write("0" + ",")

        file_out.write(str(line.split(",")[-1]))

    file_in.close()
    file_out.close()
    file_words.close()


# Main
def main():
    build_matrix()
    pass

if __name__ == '__main__':
    main()