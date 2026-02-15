from http import HTTPStatus

from fastapi import FastAPI

from schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


# mensagem
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


# cria usuarios
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    # Crie um usuário no formato do banco(array), copiando todos os dados recebidos na requisição e adicionando um id novo.
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())

    database.append(user_with_id)

    return user_with_id


# lista usuarios
@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


# editar usuario
@app.put(
    '/users/{user_id}',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
)
def update_user(user_id: int, user: UserSchema):
    # Busca um usuário no formato do banco(array), copiando todos os dados recebidos na requisição e adicionando um id novo.
    user_with_id = UserDB(id=user_id, **user.model_dump())
    # atualizar a lista
    database[user_id - 1] = user_with_id

    return user_with_id
