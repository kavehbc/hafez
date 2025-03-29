def mp3_id_formatting(id: int) -> str:
    return f"{id:04d}"


def df_to_dict(df):
    lst_poems = df.to_dict(orient='records')
    return lst_poems


def convert_arabic_to_persian(verse):
    arabic = ['ي', 'ك', 'ة']
    farsi = ['ی', 'ک', 'ه']

    for index, item in enumerate(arabic):
        verse = verse.replace(item, farsi[index])
        
    # replacing persian/farsi half-space with regular space
    verse = verse.replace(u"\u200c", " ")
    return verse
