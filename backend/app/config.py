from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str = ""
    qdrant_url: str = "http://localhost:6333"
    database_url: str = "sqlite:///../data/app.db"
    upload_dir: str = "../data/uploads"
    collection_name: str = "documents"
    embedding_model: str = "text-embedding-3-small"
    chat_model: str = "gpt-4.1-mini"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()