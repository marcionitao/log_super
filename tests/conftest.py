import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.app import app
from src.models import table_registry


# função para evitar repetição e aproveitar trecho de codigo
@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    # "create_engine", cria um ponto de contato com o DB, estabelece e gere as conexões(credenciais, uri do DB)
    engine = create_engine('sqlite:///:memory:')  # DB em memoria

    # enquanto fores rodar estes testes cria toda a estrutura do BD para mim.
    table_registry.metadata.create_all(engine)

    # a "Session" faz o meio campo entre a nossa app e o DB
    with Session(engine) as session:
        yield session

    # destrua tudo assim que terminar os testes
    table_registry.metadata.drop_all(engine)
