from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select

from database import get_session
from models import User
from schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


# mensagem
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


# cria usuarios
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session=Depends(get_session)):

    # busca se existe alguem com o email registado
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

        # criar o registo no DB
        # converter o Schema para DB
        db_user = User(
            username=user.username, email=user.email, password=user.password
        )

        # chama a session e aplica
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

    return db_user


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
    # tratando erros
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    # Busca um usuário no formato do banco(array), copiando todos os dados recebidos na requisição e adicionando um id novo.
    user_with_id = UserDB(id=user_id, **user.model_dump())
    # atualizar a lista
    database[user_id - 1] = user_with_id

    return user_with_id


# delete usuario
@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=Message
)
def delete_user(user_id: int):
    # tratando erros
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    # deleta se existir e atualizar a lista
    del database[user_id - 1]

    return {'message': 'User deleted'}
