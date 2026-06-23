from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    database_url: str
    app_name: str
    debug: bool
    api_prefix: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

