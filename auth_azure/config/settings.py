from json import load, loads
from os import environ
from typing import List, Optional, Union

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix = '', env_file='./.env')
    
    AZURE_SA: Optional[Union[dict, str]]
    GCP_SA: Optional[Union[dict, str]]
    
    CLIENT_ID: Optional[str]
    CLIENT_SECRET: Optional[str]
    AUTHORITY: Optional[str]
    REDIRECT_URI: Optional[str]
    SCOPE: List[Optional[str]]
    OUTSYSTEMS_REDIRECT_URI: Optional[str]
    
    GCP_PROJECT: Optional[str]
    GCP_DATABASE: Optional[str]
    GCP_TABLE_AUTH_STORAGE: Optional[str]
    
    DATABASE_URL: Optional[str]
    TESTS: Optional[bool] = False

    @classmethod
    def load(cls, tests: bool = False):
        from dotenv import load_dotenv
        load_dotenv()
        return cls(
            AZURE_SA=loads(environ.get('AZURE_SA')),
            GCP_SA=loads(environ.get('GCP_SA')),
            
            CLIENT_ID=environ.get('CLIENT_ID', None),
            CLIENT_SECRET=environ.get('CLIENT_SECRET', None),
            AUTHORITY=environ.get('AUTHORITY', None),
            REDIRECT_URI=environ.get('REDIRECT_URI', None),
            SCOPE=loads(environ.get('SCOPE', '[]')),
            OUTSYSTEMS_REDIRECT_URI=environ.get('OUTSYSTEMS_REDIRECT_URI', None),
            
            GCP_PROJECT=environ.get('GCP_PROJECT', None),
            GCP_DATABASE=environ.get('GCP_DATABASE', None),
            GCP_TABLE_AUTH_STORAGE=environ.get('GCP_TABLE_AUTH_STORAGE', None),
            
            DATABASE_URL=environ.get('DATABASE_URL', 'sqlite+aiosqlite:///database.db'),
            TESTS=tests,
        )


SETTINGS = Settings.load()
