from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

# --- Configuration & Settings ---

class Settings(BaseSettings):
    api_secret_key: str
    api_access_token_expire_minutes: int = 30
    database_uri: str
    debug: bool = False

    # Pydantic V2 configuration block
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False
    )

settings = Settings()

# Constants derived from settings
SECRET_KEY = settings.api_secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.api_access_token_expire_minutes

# --- Security Setup ---

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- FastAPI App ---

app = FastAPI(debug=settings.debug)

@app.get("/")
async def root():
    return {"message": "Hana Back-end API is running", "database_status": "configured"}


# app.include_router(api_router)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)