import hafez


def main():

    # it returns the total number of poems
    # returns: int
    total_number_of_poems = hafez.total_poems()
    print(f"total_number_of_poems: {total_number_of_poems}")

    # get a poem by ID
    # returns: dict
    poem_5 = hafez.get_poem(5)
    print(f"poem_5: {poem_5}")

    # get omen (fal)
    # returns: dict
    omen = hafez.omen()  # same as: hafez.fal()
    print(f"omen: {omen}")

    # search within the verses of poems
    # returns: list[dict]
    search_result = hafez.search("حافظ")
    print(f"search_result: {search_result}")


if __name__ == '__main__':
    main()
