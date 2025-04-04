from pydantic import Field
from typing_extensions import Annotated
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class DbConfigCls(BaseSettings):
    postgres_port: Annotated[int, Field(serialization_alias='POSTGRES_PORT')]
    postgres_user: Annotated[str, Field(serialization_alias='POSTGRES_USER')]
    postgres_password: Annotated[str, Field(serialization_alias='POSTGRES_PASSWORD')]
    postgres_host: Annotated[str, Field(serialization_alias='POSTGRES_HOST')]
    db_name: Annotated[str, Field(serialization_alias='DB_NAME')]


DbConfig = DbConfigCls()
