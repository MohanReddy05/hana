from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime,timedelta
from jose import JWTError,jwt
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    API_SECRETE_KEY:str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

SECRET_KEY = settings.API_SECRETE_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


app = FastAPI()

