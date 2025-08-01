import pandas as pd
import numpy as np
import pathlib
import os
import json

URI_DB_FOLDER = str(pathlib.Path(os.path.abspath(os.path.dirname(__file__))).parents[0].resolve())
URI_JSON_DB = URI_DB_FOLDER + "/data/hafez.json"


def filter_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function filters the columns of the DataFrame.
    :param df: DataFrame
    :return: DataFrame with selected columns
    """
    columns = ["id", "poem", "interpretation", "alt_interpretation", "mp3"]
    df = df[columns]
    return df

def get_data(id: int = None):

    _, df = get_connection()

    if id is not None:
        df = df[df["id"] == id]

    return df


def search_data(query: str = None, exact_match: bool = False) -> pd.DataFrame:
    query = query.strip()

    _, df = get_connection()
    df['poem_string'] = [','.join(map(str, l)) for l in df['poem']]

    if query is not None and len(query) > 0:
        if exact_match:
            lst_query = [query]
        else:
            # Split the query into words for searching
            if " " in query:
                lst_query = query.split(" ")
            else:
                lst_query = [query]

        # AND Logic
        contains = [df["poem_string"].str.contains(i) for i in lst_query]
        df = df[np.all(contains, axis=0)]

        # OR Logic
        # df = df[df["poem_string"].str.contains('|'.join(lst_query))]

    df.drop(columns=["poem_string"], inplace=True, axis=1)
    return df


def get_connection():
    with open(URI_JSON_DB, "r", encoding="utf8") as json_db:
        json_data = json.load(json_db)
    df = pd.DataFrame(json_data)
    return json_data, df
