import pickle
import pandas as pd
import json

def load_model(filename):
    with open(filename, 'rb') as f:
        model = pickle.load(f)
        return model

model = load_model('models/RandomForest.bin')

def predict(X: dict) -> int:
    X = pd.DataFrame(X, index=[0])
    y = model.predict(X)
    return y
