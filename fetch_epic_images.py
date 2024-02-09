import argparse
import os
from datetime import datetime
from save_tools import save_image
from dotenv import load_dotenv

import requests


def download_epic_pictures(api_key, args):
    params = {"count": args.count, "api_key": api_key}

    url = "https://api.nasa.gov/EPIC/api/natural/image"

    response = requests.get(url, params=params)
    response.raise_for_status()

    epic_images = response.json()

    for epic_image in epic_images:
        epic_image_date = epic_image["date"]
        file_name = epic_image["image"]
        full_name = f"{file_name}.png"
        folder = args.folder

        epic_image_date = datetime.fromisoformat(epic_image_date).strftime("%Y/%m/%d")
        path_link = f"https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{file_name}.png?api_key={api_key}"

        save_image(path_link, folder, full_name)


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

    download_epic_pictures(api_key, args)


if __name__ == "__main__":
    main()
