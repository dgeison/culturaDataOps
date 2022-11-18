import pytest
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

from fastapi.testclient import TestClient
from main import app, scaler, model

client = TestClient(app)


def testHome():
    response = client.get('/')
    assert response.json() == {'nome': 'Dgeison Serrão Peixoto'}


def testModels():
    assert isinstance(scaler, StandardScaler)
    assert isinstance(model, RandomForestClassifier)
