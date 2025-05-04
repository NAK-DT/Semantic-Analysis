from tensorflow.keras.datasets import imdb

def get_word_index():
    word_index = imdb.get_word_index()
    index_to_word = {index + 3: word for word, index in word_index.items()}

    index_to_word[0] = "<PAD>"
    index_to_word[1] = "<START>"
    index_to_word[2] = "<UNK>"
    index_to_word[3] = "<UNUSED>"

    return index_to_word

def decodeReview(sequence, index_to_word):
    return " ".join(index_to_word.get(index, "?") for index in sequence)