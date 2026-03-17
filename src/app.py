from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select

from src.database import get_session
from src.models import User
from src.schemas import Message, UserList, UserPublic, UserSchema

app = FastAPI()


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
    # now = datetime.now().isoformat()
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        # created_at=now,
    )

    # chama a session e aplica
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


# lista usuarios
@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users(limit: int = 10, offset: int = 0, session=Depends(get_session)):
    user = session.scalars(select(User).limit(limit).offset(offset))
    return {'users': user}


# editar usuario
@app.put(
    '/users/{user_id}',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
)
def update_user(user_id: int, user: UserSchema, session=Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    db_user.email = user.email
    db_user.username = user.username
    db_user.password = user.password

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


# delete usuario
@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=Message
)
def delete_user(user_id: int, session=Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    session.delete(db_user)
    session.commit()

    return {'message': 'User deleted'}
