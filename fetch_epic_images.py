import argparse
import os
from datetime import datetime
from save_tools import save_image
from dotenv import load_dotenv

import requests

load_dotenv()


def download_epic_pictures():
    parser = argparse.ArgumentParser(description='Скачка EPIC-фотографий.')
    parser.add_argument('--folder',
                        type=str,
                        default='image',
                        help='Название папки, в которую будут сохраняться EPIC-фотографии.')

    parser.add_argument('--count',
                        type=int,
                        default=5,
                        help='Количество EPIC-фото, что  нужно скачать.')

    args = parser.parse_args()

    params = {'api_key': os.environ['NASA_API_TOKEN'], 'count': args.count}

    url = 'https://api.nasa.gov/EPIC/api/natural/image'

    response = requests.get(url, params=params)
    response.raise_for_status()

    epic_images = response.json()

    for epic_image in epic_images:
        epic_image_date = epic_image['date']
        file_name = epic_image['image']

        epic_image_date = datetime.fromisoformat(epic_image_date).strftime("%Y/%m/%d")
        path_link = f"https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{file_name}.png"

        file_path = os.path.join('images', f'{file_name}.png')

        save_image(path_link, args.folder, file_path)


if __name__ == '__main__':
    download_epic_pictures()
