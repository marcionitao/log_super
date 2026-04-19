# objetivo é encriptar a password do usuario usando Hash(encriptação de via unica)
from datetime import datetime, timedelta
from http import HTTPStatus
from zoneinfo import ZoneInfo

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import decode, encode
from jwt.exceptions import PyJWTError
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from log_super.database import get_session
from log_super.models import User

pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# cria um hash "suja" da password
def get_password_hash(password: str):
    return pwd_context.hash(password)


# compara a password "limpa" com a "suja"
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# criando acesso ao token
def create_access_token(data: dict):
    to_encode = data.copy()

    # adiciona um tempo de 30 minutos para expirar
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
      minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({'exp': expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


# autorização
def get_current_user(session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
      status_code=HTTPStatus.UNAUTHORIZED,
      detail='Could not validate credentials',
      headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')
        if not username:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception

    user = session.scalar(
         select(User).where(User.email == username)
    )

    if not user:
        raise credentials_exception

    return user()
