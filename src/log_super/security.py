# objetivo é encriptar a password do usuario usando Hash(encriptação de via unica)
from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


# cria um hash "suja" da password
def get_password_hash(password: str):
    return pwd_context.hash(password)


# compara a password "limpa" com a "suja"
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
