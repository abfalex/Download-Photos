import requests
import os
import json
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote, urlparse

load_dotenv()


def get_links():
    launch_id = '5eb87d42ffd86e000604b384'

    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()

    links = response.json()['links']['flickr']['original']
    return links


def download_and_save_file(url, folder_path, index, extension):
    os.makedirs(folder_path, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    file_name = f'spacex{index}{extension}'
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'wb') as file:
        file.write(response.content)

    return file_path


def fetch_spacex_last_launch():
    links = get_links()
    for index, url in enumerate(links, start=1):
        download_and_save_file(url, './image', index)
        return url


def extract_extension_from_link(link):
    decoded_link = unquote(link)
    parsed_link = urlparse(decoded_link)
    path, fullname = os.path.split(parsed_link.path)
    file_extension_path = os.path.splitext(fullname)
    file_name, extension = file_extension_path
    return extension, file_name


def get_apod():
    parameters = {
        'api_key': os.environ['NASA_TOKEN'],
        'count': 20
    }

    response = requests.get('https://api.nasa.gov/planetary/apod', params=parameters)
    response.raise_for_status()

    data = response.json()

    return data


url = get_apod()
for index, url in enumerate(url, start=1):
    download_and_save_file(url['url'], './image', index, extract_extension_from_link(url['url'])[0])
    extract_extension_from_link(url['url'])
    print(extract_extension_from_link(url['url'])[0])



if __name__ == '__main__':
    pass
