__author__ = 'rodolfo'

# This program build a matrix based on 5 groups of popular tweets

def build_matrix():
    file_in = open("/home/rodolfo/Projetos/NeuralNetwork/pre-processing/tweet_label.txt", "r")
    file_words = open("/home/rodolfo/Projetos/NeuralNetwork/pre-processing/popular_words_w_frequency.txt", "r")

    file_out = open("/home/rodolfo/Projetos/NeuralNetwork/pre-processing/matrix_tweet_groups.txt", "w")

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

    print popular_words
    dict_matrix = {}
    count = 0
    temp_count = 0
    for line in file_in:
        temp = []

        for words in popular_words:
            for each_words in words:
                if line.split("Text:")[1].lower().split().__contains__(each_words):
                    temp_count += line.split("Text:")[1].lower().split().count(each_words)

            file_out.write(str(temp_count) + ",")
            temp_count = 0

        temp = temp + [line.split(",")[-1]]
        dict_matrix[count] = temp
        count += 1
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
