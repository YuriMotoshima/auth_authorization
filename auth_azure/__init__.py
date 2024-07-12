from msal import ConfidentialClientApplication

from auth_azure.config.collections_exceptions import collections_exceptions
from auth_azure.config.log import loginit
from auth_azure.config.settings import SETTINGS as Settings
from auth_azure.modules.token_manage import TokenStorage

try:
    loginit()
    
    msal_app = ConfidentialClientApplication(
        Settings.AZURE_SA['CLIENT_ID'],
        authority=Settings.AUTHORITY,
        client_credential=Settings.AZURE_SA['CLIENT_SECRET'],
    )
    
    TokenStorage = TokenStorage()
    
except Exception as error:
    raise collections_exceptions(error)
