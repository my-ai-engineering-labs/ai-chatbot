from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
     app_name: str = "AI Chatbot API"
     app_version: str = "1.0.0"
     app_description: str = "Backend API for the AI Chatbot project."

model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()