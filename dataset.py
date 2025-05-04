from tensorflow.keras.datasets import imdb

#example dataset from tensorflow, using imdb dataset
def loadDataset(vocab_size=10000):
    (Xtrain, ytrain), (Xtest, ytest) = imdb.load_data(num_words=vocab_size)
    return Xtrain, Xtest, ytrain, ytest