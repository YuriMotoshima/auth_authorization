from msal import ConfidentialClientApplication
from auth_azure.config.settings import SETTINGS as Settings


msal_app = ConfidentialClientApplication(
    Settings.CLIENT_ID,
    authority=Settings.AUTHORITY,
    client_credential=Settings.CLIENT_SECRET,
    
)

print()