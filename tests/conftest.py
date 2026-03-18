import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from log_super.app import app
from log_super.database import get_session
from log_super.models import User, table_registry


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


# registar um usuario para ser usado em todos os testes
@pytest.fixture
def user(session):
    user = User(username='Teste', email='test@test.com', password='testtest')

    session.add(user)
    session.commit()
    session.refresh(user)
    return user
