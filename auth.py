import os
from google_auth_oauthlib.flow import InstalledAppFlow

def login():
    """Logs in a user using Google OAuth 2.0 and returns the credentials."""
    # Define the scopes required for logging in
    scopes = [
        'openid',
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile'
    ]
    
    # Path to the client secrets file (usually downloaded from GCP Console)
    client_secrets_file = 'client_secrets.json'
    if not os.path.exists(client_secrets_file):
        raise FileNotFoundError(
            f"Please place your Google OAuth client secrets JSON file at: {os.path.abspath(client_secrets_file)}"
        )
    
    # Set up the flow using the client secrets file
    flow = InstalledAppFlow.from_client_secrets_file(
        client_secrets_file,
        scopes=scopes
    )
    
    # Run a local server to receive the authorization code redirect
    credentials = flow.run_local_server(
        host='localhost',
        port=0,
        authorization_prompt_message='Please visit this URL to authorize: {url}',
        success_message='Authorization successful! You can close this window.'
    )
    
    return credentials
