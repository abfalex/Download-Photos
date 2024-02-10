import argparse
import os
import requests
from dotenv import load_dotenv
from save_tools import extract_extension_from_link, save_image


def get_apod_images(api_key, count, folder):
    params = {
        'count': count,
        'api_key': api_key
    }

    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()

    apod_info_list = response.json()
    for index, (picture_url) in enumerate(apod_info_list, 1):
        link_to_image = picture_url.get('url')
        image_extension, image_name = extract_extension_from_link(link_to_image)
        file_name = f"apod_{index}{image_extension}"

        save_image(link_to_image, folder, file_name, api_key)


def main():
    load_dotenv()
    api_key = os.environ['NASA_API_TOKEN']

    if not api_key:
        raise ValueError("NASA_API_TOKEN не найден в переменной окружения.")

    parser = argparse.ArgumentParser(description='Скачивание APOD-фотографий.')

    parser.add_argument('--folder',
                        help="Название папки, в которую будут сохраняться фотографии.",
                        default='image',
                        type=str)

    parser.add_argument('--count',
                        help="Количество EPIC-фото, что  нужно скачать.",
                        default=5,
                        type=int)

    args = parser.parse_args()

    get_apod_images(api_key, args.count, args.folder)


if __name__ == '__main__':
    main()
