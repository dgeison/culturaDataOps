from http import client
from urllib import response
import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def testHome():
    response = client.get('/')
    assert response.json() == {'nome': 'Dgeison Serrão Peixoto'}
