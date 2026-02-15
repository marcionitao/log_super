from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    # client (conftest.py) => Arrange(organização)

    response = client.get('/')  # Act(ação)

    assert response.status_code == HTTPStatus.OK  # Assert(validação)
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user_deve_retornar_created(client):
    # client (conftest.py) => Arrange(organização)

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


def test_read_users(client):
    # client (conftest.py) => Arrange(organização)

    # Act(ação) -> UserSchema(Requisição)
    response = client.get('/users/')

    # Assert(validação) -> UserList(Resposta)
    assert response.status_code == HTTPStatus.OK
    # só pode ser executado depois do teste anterior
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@mail.com',
                'id': 1,
            }
        ]
    }


def test_update_users(client):
    # client (conftest.py) => Arrange(organização)

    # Act(ação) -> UserSchema(Requisição)
    response = client.put(
        '/users/1',
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
