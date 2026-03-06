import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from src.app import app
from src.database import get_session
from src.models import table_registry


# função que usa uma sessão de teste, ou seja um Mock
@pytest.fixture
def client(session):
    def get_sessiion_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_sessiion_override

        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    # "create_engine", cria um ponto de contato com o DB, estabelece e gere as conexões(credenciais, uri do DB)
    engine = create_engine(
        'sqlite:///:memory:',
        # permite que os testes rodem em thread diferentes
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )  # DB em memoria
    # enquanto fores rodar estes testes cria toda a estrutura do BD para mim.
    table_registry.metadata.create_all(engine)

    # a "Session" faz o meio campo entre a nossa app e o DB
    with Session(engine) as session:
        yield session

    # destrua tudo assim que terminar os testes
    table_registry.metadata.drop_all(engine)
