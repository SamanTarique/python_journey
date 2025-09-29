"""https://edabit.com/challenge/76ibd8jZxvhAwDskb"""

# [[0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0],
# [0, 0, 1, 0, 1, 0],
# [0, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 1]]


def tallest_skyscraper(sky_scrapper):

    cols = dict()

    for buildings in sky_scrapper:
        for col, val in enumerate(buildings):
            if val == 1:
                cols[col] = cols.get(col, 0) + 1

    return max(cols.values())


print(tallest_skyscraper([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]))
print(tallest_skyscraper([[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]))
print(tallest_skyscraper([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]))
