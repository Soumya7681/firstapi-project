from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME:str = "User & Project"
    DATABASE_URL:str
    SECERT_KEY:str
    ALGORITHIM:str = "HS256"
    ACCESS_TOKE_EXPIRY_MIUTES:int = 30
    UPLOAD_DIR : str = 'uploads'
    MAX_UPLOAD_SIZE_MB:int = 5

    model_config=SettingsConfigDict(env_file=".env")

settings = Settings()