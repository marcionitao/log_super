from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange(organização)

    response = client.get('/')  # Act(ação)

    assert response.status_code == HTTPStatus.OK  # Assert(validação)
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user_deve_retornar_created():
    # Arrange(organização)
    client = TestClient(app)

    # Act(ação) -> UserSchema(Requisição)
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@mail.com',
            'password': 'secret',
        },
    )

    # Assert(validação) -> UserPublic(Resposta)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@mail.com',
        'id': 1,
    }
