__author__ = 'rodolfo'

"Get predictions for one text"

import numpy as np
import cPickle as pickle

from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from sklearn.metrics import mean_squared_error as MSE


# Predict 0 or 1 to tweet. 0 means negative and 1 means not negative
def predict(isGroup):
    path_test_file = '/home/rodolfo/Projetos/NeuralNetwork/data/test_groups_%s_file.csv' % isGroup
    path_neural_network = 'model_groups_%s.pkl' % isGroup

    test_file = path_test_file
    model_file = path_neural_network
    output_predictions_file = 'predictions_file.txt'

    # load model
    net = pickle.load(open(model_file, 'rb'))

    # load data
    test = np.loadtxt(test_file, delimiter=',')
    x_test = test[:,0:-1]
    y_test = test[:,-1]
    y_test = y_test.reshape(-1, 1)

    # you'll need labels. In case you don't have them...
    y_test_dummy = np.zeros( y_test.shape )

    input_size = x_test.shape[1]
    target_size = y_test.shape[1]

    assert( net.indim == input_size )
    assert( net.outdim == target_size )

    # prepare dataset
    ds = SDS( input_size, target_size )
    ds.setField( 'input', x_test )
    ds.setField( 'target', y_test_dummy )

    # predict
    p = net.activateOnDataset( ds )
    np.savetxt( output_predictions_file, p, fmt = '%.6f' )


# This program build a matrix based on 5 groups of popular tweets
def build_matrix(popular_words, string, isGroup):
    text = string
    path = '/home/rodolfo/Projetos/NeuralNetwork/data/test_groups_%s_file.csv' % isGroup
    file_out = open(path, 'a+')

    print "\nMatrix:\n"
    if isGroup:
        temp_count = 0
        for words in popular_words:
            for each_words in words:
                if text.__contains__(each_words):
                    temp_count += text.lower().split().count(each_words)

            print str(words) + " = " + str(temp_count)
            file_out.write(str(temp_count) + ",")
            temp_count = 0

        file_out.write("0\n")
    else:
        for words in popular_words:
            if text.lower().split().__contains__(words):
                n_words = text.lower().split().count(words)
                file_out.write(str(n_words) + ",")
                print str(words) + " = " + str(n_words)
            else:
                file_out.write("0" + ",")
        file_out.write("0\n")

    file_out.close()


# Build one matrix 1x1
def build_popular_list(isGroup):
    file_words = open("/home/rodolfo/Projetos/NeuralNetwork/pre-processing/popular_words_w_frequency.txt", "r")

    popular_words = []

    if isGroup:
        popular_words_temp = []
        count = 1
        for line in file_words:
            if count < 5:
                popular_words_temp = popular_words_temp + [line.split("'")[1]]
                count += 1
            else:
                popular_words_temp = popular_words_temp + [line.split("'")[1]]
                popular_words = popular_words + [popular_words_temp]
                count = 1
                popular_words_temp = []

    else:
        for line in file_words:
            popular_words = popular_words + [line.split("'")[1]]

    file_words.close()
    return popular_words


# Main
def main():
    while True:
        print "Which Neural Network do you want to use?"
        print "1) Regular"
        print "2) Groups\n"
        option = raw_input(":")

        isgroup = True
        if option.__eq__("1") or option.__eq__("2"):
            tweet = raw_input('\nPlease, tell me which tweet I should evaluate: ')

            print "---"*20
            if option.__eq__("1"):
                isgroup = False

            build_matrix(build_popular_list(isgroup), tweet, isgroup)
            predict(isgroup)

            file_answer = open('predictions_file.txt', "r")
            answer = file_answer.readlines()[-1]
            print answer
            if float(answer) > 0.5:
                print "This tweet: ''%s''is not negative \n" % tweet
            else:
                print "This tweet: ''%s''is negative \n" % tweet

            print "---"*20

        else:
            break


if __name__ == '__main__':
    main()