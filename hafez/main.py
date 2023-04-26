import random
from hafez.utils.db import get_data, search_data
from hafez.utils.formating import df_to_dict


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
