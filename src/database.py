from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.settings import Settings

# criando uma engine e conectando com o DB
engine = create_engine(Settings().DATABASE_URL)


# criando uma Session
# a "Session" faz o meio campo entre a nossa app e o DB
# pragma: no cover -> info para não testar
def get_session():  # pragma: no cover
    with Session(engine) as session:
        yield session  # fecha a session
