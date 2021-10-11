from telethon.sync import TelegramClient
from plugins.utils import Config

config_manager = Config()

api_id = config_manager.get('api_id')
api_hash = config_manager.get('api_hash')


def get_client():
    client = TelegramClient('client', api_id, api_hash)
    return client
