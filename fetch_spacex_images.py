import requests
import argparse
from save_tools import save_image


def get_last_images():
    parser = argparse.ArgumentParser(description='Скачивание фотографий определенных запусков SpaceX.')
    parser.add_argument('--id',
                        help="Укажите ID запуска",
                        default='5eb87d42ffd86e000604b384',
                        type=str)

    parser.add_argument('--folder',
                        type=str,
                        default='image',
                        help='Укажите название папки, в которую будут сохраняться фотографии.')

    args = parser.parse_args()

    url = f'https://api.spacexdata.com/v5/launches/{args.id}'

    response = requests.get(url)
    response.raise_for_status()

    links = response.json()['links']['flickr']['original']

    filename = 'spaceX_'

    for index, pictures in enumerate(links, 1):
        full_name = f"{filename}{index}.jpg"
        save_image(url, args.folder, full_name)


if __name__ == '__main__':
    get_last_images()
