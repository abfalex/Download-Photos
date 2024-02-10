import requests
import argparse
from save_tools import save_image


def get_last_images(launch_id, folder):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    response = requests.get(url)
    response.raise_for_status()

    flickr_original_links = response.json()['links']['flickr']['original']

    for index, picture_url in enumerate(flickr_original_links, 1):
        full_name = f"spaceX_{index}.jpg"

        save_image(picture_url, folder, full_name)


def main():
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

    get_last_images(args.id, args.folder)


if __name__ == '__main__':
    main()
