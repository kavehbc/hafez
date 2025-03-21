def mp3_id_formatting(id: int) -> str:
    return f"{id:04d}"


def df_to_dict(df):
    lst_poems = []
    for index, row in df.iterrows():
        poem_id = row["id"]
        str_poem = row["Poem"]
        lst_verses = str_poem.split("\\r\\n")
        if "" in lst_verses:
            lst_verses.remove("")

        str_interpretation = row["Interpretation"]
        str_alt_interpretation = row["alt_interpretation"]
        dic_poem = {"id": poem_id,
                    "poem": lst_verses,
                    "interpretation": str_interpretation,
                    "alt_interpretation": str_alt_interpretation,
                    "mp3": f"https://de.loveziba.com/2019/10/{mp3_id_formatting(poem_id)}.mp3"}
        lst_poems.append(dic_poem)
    return lst_poems


def convert_arabic_to_persian(verse):
    arabic = ['ي', 'ك', 'ة']
    farsi = ['ی', 'ک', 'ه']

    for index, item in enumerate(arabic):
        verse = verse.replace(item, farsi[index])
        
    # replacing persian/farsi half-space with regular space
    verse = verse.replace(u"\u200c", " ")
    return verse
