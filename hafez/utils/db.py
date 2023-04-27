import pandas as pd
import sqlite3
from sqlite3 import Connection
import pathlib
import os


URI_SQLITE_DB = str(pathlib.Path(os.path.abspath(os.path.dirname(__file__))).parents[0].resolve()) + "/data/hafez.db"


def get_data(id: int = None):
    conn = get_connection()
    if id is None:
        sql_query = "SELECT * FROM poems"
    else:
        sql_query = f"SELECT * FROM poems WHERE id = {id}"

    df = pd.read_sql(sql_query, con=conn)
    return df


def search_data(query: str = None):
    conn = get_connection()
    if query is None or len(query) == 0:
        sql_query = "SELECT * FROM poems"
    else:
        lst_query = query.split(" ")
        sql_query = f"SELECT * FROM poems WHERE"
        i = 0
        for item in lst_query:
            if i > 0:
                sql_query += f" AND"
            sql_query += f" Poem LIKE '%{item}%'"
            i += 1

    df = pd.read_sql(sql_query, con=conn)
    return df


def get_connection() -> Connection:
    """Put the connection in cache to reuse if path does not change between Streamlit reruns.
    NB : https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa
    """
    return sqlite3.connect(URI_SQLITE_DB, check_same_thread=False)
