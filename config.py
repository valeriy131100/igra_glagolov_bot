import json

from environs import Env


env = Env()
env.read_env()
telegram_token = env.str('TELEGRAM_TOKEN')

google_credentials_path = env.str('GOOGLE_APPLICATION_CREDENTIALS')

with open(google_credentials_path, 'r') as credentials_file:
    credentials = json.load(credentials_file)
dialogflow_project_id = credentials['project_id']
