from pydantic_settings import BaseSettings,SettingConfigDict


class Settings(BaseSettings):
    api_secret_key: str
    api_access_token_expire_minutes: int = 30
    database_uri: str
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra = "ignore",
        case_sensitive = False
    )

settings = Settings()