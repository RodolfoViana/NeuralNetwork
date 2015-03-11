__author__ = 'rodolfo'


# This program build a matrix based on 5 groups of popular tweets
def build_matrix(popular_words):
    file_in = open("/home/rodolfo/Projetos/NeuralNetwork/pre-processing/tweet_label.txt", "r")
    file_out = open("/home/rodolfo/Projetos/NeuralNetwork/pre-processing/matrix_tweet_groups2.txt", "w")

    temp_count = 0
    for line in file_in:
        for words in popular_words:
            for each_words in words:
                if line.split("Text:")[1].lower().split().__contains__(each_words):
                    temp_count += line.split("Text:")[1].lower().split().count(each_words)

            file_out.write(str(temp_count) + ",")
            temp_count = 0

        file_out.write(str(line.split(",")[-1]))

    file_out.close()
    file_in.close()


#Build a list with popular words
def buildPopularList():
    file_words = open("/home/rodolfo/Projetos/NeuralNetwork/pre-processing/popular_words_w_frequency.txt", "r")

    popular_words = []

    popular_words_temp = []
    count = 0
    for line in file_words:
        if count < 5:
            popular_words_temp = popular_words_temp + [line.split("'")[1]]
            count += 1
        else:
            popular_words = popular_words + [popular_words_temp]
            count = 1
            popular_words_temp = []
            popular_words_temp = popular_words_temp + [line.split("'")[1]]
    popular_words = popular_words + [popular_words_temp]


    file_words.close()
    return popular_words


# Main
def main():
    build_matrix(buildPopularList())
    pass


if __name__ == '__main__':
    main()
