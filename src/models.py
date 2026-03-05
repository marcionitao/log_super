from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'
    # init=False -> aciona o auto increment & chave primaria(PK)
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        # server_default=func.now() -> server busca a hora do sistema onde ele está a executar
        init=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        # onupdate=func.now() -> atualiza a hora do sistema onde ele está a executar
        init=False,
        onupdate=func.now(),
    )
