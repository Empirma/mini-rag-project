from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    
    MONGODB_URL: str
    MONGODB_DATABASE: str

    GENERATION_BACKEND: str
    EMBEDDING_BACKEND: str

    OPENAI_API_KEY: Optional[str] = None
    OPENAI_API_URL: Optional[str] = None
    COHERE_API_KEY: Optional[str] = None
    COHERE_API_URL: Optional[str] = None

    GENERATION_MODEL_ID: Optional[str] = None
    EMBEDDING_MODEL_ID: Optional[str] = None
    EMBEDDING_MODEL_SIZE: Optional[int] = None
    INPUT_DEFAULT_MAX_CHARACTERS: Optional[int] = None
    GENERATION_DEFAULT_MAX_TOKENS: Optional[int] = None
    GENERATION_DEFAULT_TEMPERATURE: Optional[float] = None


    VECTOR_DB_BACKEND: str
    VECTOR_DB_NAME: str
    VECTOR_DB_DISTANCE_METHOD: str


    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
