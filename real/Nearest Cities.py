from collections import defaultdict


class City:
    def __init__(self, cityName, x, y):
        self.name = cityName
        self.x = x
        self.y = y

    def dist(self, p2):
        return (self.x - p2.x) ** 2 + (self.y - p2.y) ** 2


def near(numOfCities, cities, xCoord, yCoord, numQueries, queries):
    central = zip(cities, xCoord, yCoord)

    cityMap = {}
    xHash = defaultdict(list)
    yHash = defaultdict(list)

    for city, x, y in central:
        curr = City(city, x, y)
        cityMap[city] = curr
        xHash[x].append(curr)
        yHash[y].append(curr)

    output = []
    query_cache = {}

    for city in queries:
        # check if in query cache
        query = cityMap[city]
        xVals = xHash[query.x]
        yVals = yHash[query.y]

        matches = xVals + yVals

        nearest = None

        if len(matches) > 2:
            matches.sort(key=lambda x: x.dist(query))
            matches = [x.name for x in matches]
            nearest = matches[2]

        output.append(nearest)

    return output


def euc(tup1, tup2):
    # without sqroot, (x2-x1) ** 2 + (y2 - y1) ** 2
    return (tup1[0] - tup2[0]) ** 2 + (tup1[1] - tup2[1]) ** 2


numOfCities = 3

cities = ["c1", "c2", "c3"]

xCoordinates = [3, 2, 1]

yCoordinates = [3, 2, 3]

numOfQueries = 3

queries = ["c1", "c2", "c3"]

print(near(numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries))