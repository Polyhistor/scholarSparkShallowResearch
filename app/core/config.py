from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "shallowresearchscholarspark"
    DEBUG: bool = False
    PORT: int = 8000
    
    class Config:
        env_file = ".env"

settings = Settings()