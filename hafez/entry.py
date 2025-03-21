import random
from typing import Tuple, Optional
import requests
import os
import pathlib
from hafez.utils.db import get_data, search_data
from hafez.utils.formating import df_to_dict

URI_MP3_FOLDER = str(
        pathlib.Path(os.path.abspath(os.path.dirname(__file__))).resolve()) + "/data/audio"


def get_mp3_url(poem):
    # base_url = "https://de.loveziba.com/2019/10"
    base_url = "https://raw.githubusercontent.com/kavehbc/hafez/master/data/audio/"

    mp3_filename = f"{poem:04d}.mp3"
    url = base_url + mp3_filename

    return mp3_filename, url


def download_all_audio(force=False) -> int:
    """
    This function downloads the MP3 files and saves them locally.
    :return: total number of files saved
    """
    for poem_number in range(1, 496):
        get_audio(poem=poem_number, download=force)
        yield poem_number


def download_audio(poem=1) -> tuple[Optional[int], str, str]:
    """
    This function downloads a MP3 file and saves it locally.
    :param poem: number of poem. Defaults to 1
    :return: 1
    """
    mp3_filename, url = get_mp3_url(poem)

    with requests.Session() as req:
        status = None
        mp3_path = f'{URI_MP3_FOLDER}/{mp3_filename}'
        download = req.get(url)
        if download.status_code == 200:
            try:
                with open(mp3_path, 'wb') as f:
                    f.write(download.content)
                    status = 1
            except:
                status = 0

    return status, mp3_path, url


def get_audio(poem=1, download=True) -> str:
    """
    This function retrieve MP3 file of a poem.
    :param poem: poem number. Defaults to 1
    :param download: Download if the file does not exist. Defaults to True
    :return: MP3 file absolute path
    """
    mp3_filename = f"{poem:04d}.mp3"
    path = f'{URI_MP3_FOLDER}/{mp3_filename}'

    return_value = None

    if not os.path.exists(path) and download:
        status, local_path, url = download_audio(poem=poem)
        if status == 0:
            # local saving failed
            return_value = url
        elif status == 1:
            # file successfully saved locally
            return_value = local_path
    elif not os.path.exists(path) and not download:
        mp3_filename, url = get_mp3_url(poem)
        return_value = url
    else:
        return_value = os.path.abspath(path)

    return return_value


def total_poems() -> int:
    """
    This function return the total number of available poems of Hafez
    :return: an integer showing the total number of poems
    """
    return 495


def get_poem(poem_id) -> dict:
    """
    This function retrieves a poem by ID
    :param poem_id: this is poem ID between 1 and total_poems()
    :return: a dictionary containing the poem verses and its interpretation
    """
    df = get_data(poem_id)
    lst_poem = df_to_dict(df)

    return lst_poem[0]


def search(query) -> list:
    """
    It searches through the verses of Divan and once a record found, it returns the whole poem.
    :param query: the string term to query into Divan
    :return: a list of dictionary containing all the poems which have the queried terms
    """
    df = search_data(query)
    lst_poem = df_to_dict(df)

    return lst_poem


def omen() -> dict:
    """
    Omen or Fal returns a random poem
    :return: a dictionary of poem
    """
    poem_id = random.randint(1, total_poems())
    return get_poem(poem_id)


def fal() -> dict:
    """
    Omen or Fal returns a random poem
    :return: a dictionary of poem
    """
    return omen()
