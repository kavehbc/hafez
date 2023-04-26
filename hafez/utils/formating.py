def mp3_id_formatting(id):
    if id < 10:
        str_id = "000" + str(id)
    elif 10 <= id < 100:
        str_id = "00" + str(id)
    elif 100 <= id < 1000:
        str_id = "0" + str(id)
    return str_id


def df_to_dict(df):
    lst_poems = []
    for index, row in df.iterrows():
        poem_id = row["id"]
        str_poem = row["Poem"]
        lst_verses = str_poem.split("\\r\\n")
        if "" in lst_verses:
            lst_verses.remove("")

        str_interpretation = row["Interpretation"]
        dic_poem = {"id": poem_id,
                    "poem": lst_verses,
                    "interpretation": str_interpretation,
                    "mp3": f"https://de.loveziba.com/2019/10/{mp3_id_formatting(poem_id)}.mp3"}
        lst_poems.append(dic_poem)
    return lst_poems
