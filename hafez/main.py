import random
from hafez.utils.db import get_data, search_data
from hafez.utils.formating import df_to_dict


def total_poems():
    return 495


def get_poem(poem_id):
    df = get_data(poem_id)
    lst_poem = df_to_dict(df)

    return lst_poem[0]


def search(query):
    df = search_data(query)
    lst_poem = df_to_dict(df)

    return lst_poem


def omen():
    poem_id = random.randint(1, total_poems())
    return get_poem(poem_id)


def fal():
    return omen()
