import argparse
import os
from datetime import datetime
from save_tools import save_image
from dotenv import load_dotenv

import requests


def download_epic_pictures(api_key, count, folder):
    epic_params = {"count": count, "api_key": api_key}
    epic_url = "https://api.nasa.gov/EPIC/api/natural/image"

    epic_response = requests.get(epic_url, params=epic_params)
    epic_response.raise_for_status()

    epic_images = epic_response.json()

    for epic_image in epic_images:
        epic_image_date = epic_image.get('date')
        file_name = epic_image.get('image')
        full_name = f"{file_name}.png"

        image_date_formatted = datetime.fromisoformat(epic_image_date).strftime("%Y/%m/%d")

        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date_formatted}/png/{file_name}.png"
        image_params = {"api_key": api_key}

        image_response = requests.get(image_url, params=image_params)
        image_response.raise_for_status()

        save_image(image_response.url, folder, full_name)


def main():
    load_dotenv()
    api_key = os.environ["NASA_API_TOKEN"]

    if not api_key:
        raise ValueError("NASA_API_TOKEN не найден в переменной окружения.")

    parser = argparse.ArgumentParser(description="Скачивание EPIC-фотографий.")
    parser.add_argument("--folder",
                        type=str,
                        default="image",
                        help="Название папки, в которую будут сохраняться EPIC-фотографии.")

    parser.add_argument("--count",
                        type=int,
                        default=5,
                        help="Количество EPIC-фото, что  нужно скачать.")

    args = parser.parse_args()

    download_epic_pictures(api_key, args.count, args.folder)


if __name__ == "__main__":
    main()
