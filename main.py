import os
import pickle
from fastapi import FastAPI


def loadModels():
    model = pickle.load(
        open(os.path.join(os.getcwd(), 'models', 'model.pkl'), 'rb'))
    scaler = pickle.load(
        open(os.path.join(os.getcwd(), 'models', 'scaler.pkl'), 'rb'))

    return scaler, model


scaler, model = loadModels()
app = FastAPI()


@app.get('/')
def function():
    return {'nome': 'Dgeison Serrão Peixoto'}
