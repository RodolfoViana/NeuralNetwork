__author__ = 'rodolfo'

"Get predictions for one text"

import numpy as np
import cPickle as pickle

from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from sklearn.metrics import mean_squared_error as MSE


# Predict 0 or 1 to tweet. 0 means negative and 1 means not negative
def predict():
    test_file = '/home/rodolfo/Projetos/NeuralNetwork/data/test_groups.csv'
    model_file = 'model_groups.pkl'
    output_predictions_file = 'predictions_groups.txt'

    # load model

    net = pickle.load( open( model_file, 'rb' ))

    # load data

    test = np.loadtxt( test_file, delimiter = ',' )
    x_test = test[:,0:-1]
    y_test = test[:,-1]
    y_test = y_test.reshape( -1, 1 )

    # you'll need labels. In case you don't have them...
    y_test_dummy = np.zeros( y_test.shape )

    input_size = x_test.shape[1]
    target_size = y_test.shape[1]

    assert( net.indim == input_size )
    assert( net.outdim == target_size )

    # prepare dataset

    print y_test_dummy[0]

    ds = SDS( input_size, target_size )
    ds.setField( 'input', x_test )
    ds.setField( 'target', y_test_dummy )

    # predict

    p = net.activateOnDataset( ds )

    mse = MSE( y_test, p )
    rmse = sqrt( mse )

    print "testing RMSE:", rmse

    np.savetxt( output_predictions_file, p, fmt = '%.6f' )


# This program build a matrix based on 5 groups of popular tweets
def build_matrix(popular_words, string):
    text = string
    file_out = ""

    temp_count = 0
    for words in popular_words:
        for each_words in words:
            if text.__contains__(each_words):
                temp_count += text.lower().split().count(each_words)

        file_out = file_out + str(temp_count) + ","
        temp_count = 0

    file_out = file_out + str(text.split(",")[-1])
    print file_out
    return file_out


# Build one matrix 1x1
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
    tweet = raw_input('Please, tell me which tweet I should evaluate: ')
    tweet = tweet + ",0"

    build_matrix(buildPopularList(), tweet)
    pass


if __name__ == '__main__':
    main()