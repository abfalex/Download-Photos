import argparse
import os
import requests
from dotenv import load_dotenv
from save_tools import extract_extension_from_link, download_and_save_file

load_dotenv()


def get_apod_images():
    parser = argparse.ArgumentParser(description='Скачка APOD-фотографий.')

    parser.add_argument('--folder',
                        help="Название папки, в которую будут сохраняться фотографии.",
                        default='./image',
                        type=str)

    parser.add_argument('--count',
                        help="Количество EPIC-фото, что  нужно скачать.",
                        default=5,
                        type=int)

    args = parser.parse_args()

    parameters = {
        'api_key': os.environ['NASA_API_KEY'],
        'count': args.count
    }

    response = requests.get('https://api.nasa.gov/planetary/apod', params=parameters)
    response.raise_for_status()

    data = response.json()

    for index, url in enumerate(data, 1):
        link_to_image = url['url']
        image_extension = extract_extension_from_link(link_to_image)[0]
        folder_path = args.folder

        download_and_save_file(link_to_image, folder_path, index, image_extension)
        extract_extension_from_link(link_to_image)


if __name__ == '__main__':
    get_apod_images()
