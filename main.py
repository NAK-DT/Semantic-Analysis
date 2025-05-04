import warnings
warnings.filterwarnings('ignore')
from dataset import loadDataset
from preprocessing import padding, splitData
from utils import get_word_index, decodeReview
from model import lstmmodel

X, y = loadDataset()

X_train, X_val, X_test, y_train, y_val, y_test = splitData(X, y)
X_train = padding(X_train, maxlen=500, padding='pre', truncating='pre', value=0)
X_val   = padding(X_val, maxlen=500, padding='pre', truncating='pre', value=0)
X_test  = padding(X_test, maxlen=500, padding='pre', truncating='pre', value=0)

index_to_word = get_word_index()
print(decodeReview(X_train[0], index_to_word))
print("Label:", y_train[0])

model = lstmmodel()
model.summary()

