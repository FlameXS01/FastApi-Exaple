from pydantic_settings import BaseSettings  

class Settings (BaseSettings):
    PROJEC_NAME :str = "FastAPI-Blog"
    PROJEC_VERSION :str = "0.0.1"
    DATABASE_URL :str
    
    class Config:
        env_file = ".env"
        
settings = Settings()