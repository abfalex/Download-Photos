import os
import requests
from urllib.parse import unquote, urlparse


def save_image(url, folder_path, file_name, api_key=''):
    os.makedirs(folder_path, exist_ok=True)

    response = requests.get(url, params=api_key)
    response.raise_for_status()

    full_name = os.path.join(folder_path, file_name)

    with open(full_name, 'wb') as file:
        file.write(response.content)


def download_and_save_file(url, folder_path, index, extension):
    os.makedirs(folder_path, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    file_name = f'spacex{index}{extension}'
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'wb') as file:
        file.write(response.content)

    return file_path


def extract_extension_from_link(link):
    decoded_link = unquote(link)
    parsed_link = urlparse(decoded_link)
    path, fullname = os.path.split(parsed_link.path)
    file_extension_path = os.path.splitext(fullname)
    file_name, extension = file_extension_path
    return extension, file_name
