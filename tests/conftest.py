import pytest
from fastapi.testclient import TestClient

from src.app import app


# função para evitar repetição e aproveitar trecho de codigo
@pytest.fixture
def client():
    return TestClient(app)
