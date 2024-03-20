from time import sleep
from telethon.sync import TelegramClient, events
from telethon import TelegramClient, sync


trechos = ["3200 MHZ", "3200MHZ", "4600G", "A520", "500W", "GABINETE"]

api_id = 23649447
api_hash = 'e688edbc3db154b25370165c872a9e5c'
bot_token = '6229798078:AAGcQvKWEYOhDw_vj1WeqMQOvlXxzDySR9s'

with TelegramClient('california', api_id, api_hash) as client:
    with TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token) as bot:
            
        destination_user_username = 'santtt' 
        
        entity = client.get_entity(destination_user_username)
        
        chats = [-1001634454625, -1001283210985, -1001352231186]
        for chat in chats:
            ultima_msg = client.get_messages(chat, limit=1)[0].id
            for message in client.get_messages(chat, limit=25, offset_id = ultima_msg):
                for trecho in trechos:
                    try:
                        if (trecho in message.message):
                            destination_user_username = 'santtt'
                            entity = bot.get_entity(destination_user_username)
                            bot.send_message(entity=entity, message=message.message)
                            sleep(10)
                    except:
                        pass

    client.run_until_disconnected()

