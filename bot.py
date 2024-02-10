import logging
import os
import random
import asyncio
import argparse

from aiogram import Dispatcher, Bot, types
from dotenv import load_dotenv


async def main():
    load_dotenv()

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')

    bot = Bot(token=tg_bot_token)
    dp = Dispatcher()

    parser = argparse.ArgumentParser(description='Отправка изображений в Телеграм-канал')
    parser.add_argument('--time',
                        type=int,
                        default=5,
                        help='Задержка между отправкой сообщений')
    parser.add_argument('--folder',
                        type=str,
                        default='image',
                        help='Путь к директории с изображениями')

    args = parser.parse_args()
    time = args.time
    photo_directory = args.folder

    while True:
        photo_files = [os.path.join(name_file, file) for name_file, _, files in os.walk(photo_directory) for file in
                       files]

        if not photo_files:
            logging.info(f'Папка {photo_directory} пуста.')
            break

        random_photo = random.choice(photo_files)

        with open(random_photo, 'rb'):
            input_file = types.FSInputFile(random_photo)
            await bot.send_photo(chat_id=tg_chat_id, photo=input_file)
            logging.info(f'Отправка фотографии: {random_photo}')

        await asyncio.sleep(time)

    await asyncio.gather(dp.start_polling(bot), main())


if __name__ == '__main__':
    asyncio.run(main())
