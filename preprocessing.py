from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

#simple preprocessing, for now only truncating and padding sequences
def padding(sequences, maxlen=500, padding='pre', truncating='pre', value=0):
    return pad_sequences(sequences, maxlen=maxlen, padding=padding, truncating=truncating, value=value)

def splitData(X, y, val_size=0.2, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=True)

    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=val_size, random_state=random_state, shuffle=True)

    return X_train, X_val, X_test, y_train, y_val, y_test