from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME:str = "User & Product"
    DATABASE_URL:str
    SECERT_KEY:str
    ALGORITHIM:str = "HS256"
    ACCESS_TOKE_EXPIRY_MIUTES:int = 30
    UPLOAD_DIR : str = 'uploads'
    MAX_UPLOAD_SIZE_MB:int = 5
    DB_POOL_SIZE:int = 5
    DB_MAX_OVERFLOW:int = 10

    model_config=SettingsConfigDict(env_file=".env")

settings = Settings()