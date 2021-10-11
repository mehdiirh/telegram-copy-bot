from telethon.sync import TelegramClient


api_id = 232090
api_hash = 'b87cb412a56dfd3ed52e38ff40c6b52d'


def get_client():
    client = TelegramClient('client', api_id, api_hash)
    return client
