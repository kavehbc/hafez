import hafez


def main():

    # it returns the total number of poems
    # returns: int
    total_number_of_poems = hafez.total_poems()

    # get a poem by ID
    # returns: dict
    poem_5 = hafez.get_poem(5)

    # get omen (fal)
    # returns: dict
    omen = hafez.omen()  # same as: hafez.fal()

    # search within the verses of poems
    # returns: list[dict]
    search_result = hafez.search("حافظ")


if __name__ == '__main__':
    main()
