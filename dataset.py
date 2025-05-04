from tensorflow.keras.datasets import imdb

#example dataset from tensorflow, using imdb dataset
def loadDataset(vocab_size=10000):
    (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocab_size)
    return X_train, X_test, y_train, y_test

