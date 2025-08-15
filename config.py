from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, HttpUrl, DirectoryPath, FilePath, BaseModel
from typing import Self
from enum import Enum


class Browser(str, Enum):
    CHROMIUM = 'chromium'
    WEBKIT = 'webkit'
    FIREFOX = 'firefox'

class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    tracing_dir: DirectoryPath
    browser_state_file: FilePath

    @classmethod
    def initialize(cls) -> Self:
        tracing_dir = DirectoryPath("./tracing")
        browser_state_file = FilePath("browser-state.json")

        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            tracing_dir=tracing_dir,
            browser_state_file=browser_state_file
        )

settings = Settings.initialize()