import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings('ignore')
from dataset import loadDataset
from preprocessing import padding, splitData
from utils import get_word_index, decodeReview
from model import lstmmodel, nnmodel
from train import train, evaluate, plot_history

X, y = loadDataset()

X_train, X_val, X_test, y_train, y_val, y_test = splitData(X, y)
X_train = padding(X_train, maxlen=500, padding='pre', truncating='pre', value=0)
X_val   = padding(X_val, maxlen=500, padding='pre', truncating='pre', value=0)
X_test  = padding(X_test, maxlen=500, padding='pre', truncating='pre', value=0)

index_to_word = get_word_index()
print(decodeReview(X_train[0], index_to_word))
print("Label:", y_train[0])

model_type = "nn"

if model_type == "lstm":
    model = lstmmodel()
elif model_type == "nn":
    model = nnmodel()
else:
    raise ValueError("Invalid model type. Choose 'lstm' or 'nn'.")
model.build(input_shape=(None, 500))
model.summary()

history = train(model, X_train, y_train, X_val, y_val, epochs=10, batch_size=32)
evaluate(model, X_test, y_test)
plot_history(history)

