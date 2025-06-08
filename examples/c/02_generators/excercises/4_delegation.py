# def city_generator():
#     cities = ['Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Ruse', 'Stara Zagora', 'Pleven', 'Sliven', 'Dobrich', 'Shumen']
#     for x in cities:
#         yield x


def city_ranking(n=1):

    def city_generator():
        cities = ['Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Ruse', 'Stara Zagora', 'Pleven', 'Sliven',
                  'Dobrich', 'Shumen']
        for x in cities:
            yield x

    g = city_generator()
    for x in range(n):
        yield next(g)


for city in city_ranking(n=5):
    print(city)
