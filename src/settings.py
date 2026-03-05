from pydantic_settings import BaseSettings, SettingsConfigDict

#  o objetivo é ter um local central, seguro e tipado para “ler” configurações, com validação automática e carregamento de variáveis de ambiente, evitando espalhar os.getenv() pelo código.


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    # declare the values your app needs
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URL: str
