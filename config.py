# from pydantic import BaseSettings

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
import os
import pathlib

file_env = str(pathlib.Path(__file__).parent.absolute())
file_env = file_env + '\.env'

class Settings(BaseSettings):
    CMC_API_KEY: str
    DOMINANCE_STATISTIC_FILE: str = "filename1.csv"

    model_config = SettingsConfigDict(env_file=[file_env])


settings = Settings()

