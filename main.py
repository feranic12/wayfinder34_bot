from bot_handler import BotHandler
from time import sleep


def main():
    my_bot = BotHandler("977156718:AAGCGjJ46G1J4XIqdf62DY6PuXwFPu9iMxM")
    update_id = my_bot.get_last_update()['update_id']
    while True:
        if update_id == my_bot.get_last_update()['update_id']:
            my_bot.send_message(my_bot.get_chat_id(my_bot.get_last_update()), 'test')
            update_id += 1
        sleep(1)


if __name__ == '__main__':
    main()