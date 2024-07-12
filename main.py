from msal import ConfidentialClientApplication

from auth_azure.config.settings import SETTINGS as Settings

msal_app = ConfidentialClientApplication(
    Settings.AZURE_SA['CLIENT_ID'],
    authority=Settings.AUTHORITY,
    client_credential=Settings.AZURE_SA['CLIENT_SECRET'],
    
)

print()