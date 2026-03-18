from sqlalchemy import select

from log_super.models import User


def test_create_user(session):

    # session (conftest.py) => Arrange(organização)

    user = User(username='Marcio', email='marcio@mail.com', password='12345')
    # adicionando o 'user' a sessão
    session.add(user)
    session.commit()
    # Scalar possibilita fazer uma query no DB injetando SQL comandos e retorna um Objeto
    result = session.scalar(
        select(User).where(User.email == 'marcio@mail.com')
    )

    assert result.username == 'Marcio'
