from json import load, loads
from os import environ, path
from sys import platform
from typing import List, Optional, Union

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict()
    
    CLIENT_ID: Optional[str]
    CLIENT_SECRET: Optional[str]
    AUTHORITY: Optional[str]
    REDIRECT_URI: Optional[str]
    SCOPE: List[Optional[str]]
    OUTSYSTEMS_REDIRECT_URI: Optional[str]
    GCP_SA: Optional[Union[dict, str]]
    AZURE_SA: Optional[Union[dict, str]]
    GCP_PROJECT: Optional[str]
    GCP_DATABASE: Optional[str]
    GCP_TABLE_AUTH_STORAGE: Optional[str]
    DATABASE_URL: Optional[str]
    TESTS: Optional[bool] = False

    class Config:
        env_prefix = ''  # Evita adicionar um prefixo 'APP_' às variáveis de ambiente

    @classmethod
    def load(cls, tests: bool = False):
        app_config = {}
        app_azure = {}
        if (platform in ['win32', 'win64']):
            from dotenv import load_dotenv
            load_dotenv()
            if path.isfile('./login.json'):
                with open('./login.json') as config_file:
                    app_config = load(config_file) or {}
            if path.isfile('./azure_data.json'):
                with open('./azure_data.json') as config_file:
                    app_azure = load(config_file) or {}

        return cls(
            CLIENT_ID=environ.get('CLIENT_ID', None),
            CLIENT_SECRET=environ.get('CLIENT_SECRET', None),
            AUTHORITY=environ.get('AUTHORITY', None),
            REDIRECT_URI=environ.get('REDIRECT_URI', None),
            SCOPE=loads(environ.get('SCOPE', '[]')),
            OUTSYSTEMS_REDIRECT_URI=environ.get('OUTSYSTEMS_REDIRECT_URI', None),
            GCP_SA=loads(environ.get('GCP_SA')) if environ.get('GCP_SA') else app_config,
            AZURE_SA=loads(environ.get('AZURE_SA')) if environ.get('AZURE_SA') else app_azure,
            GCP_PROJECT=environ.get('GCP_PROJECT', None),
            GCP_DATABASE=environ.get('GCP_DATABASE', None),
            GCP_TABLE_AUTH_STORAGE=environ.get('GCP_TABLE_AUTH_STORAGE', None),
            DATABASE_URL=environ.get('DATABASE_URL', 'sqlite:///database.db'),
            TESTS=tests,
        )


SETTINGS = Settings.load()
