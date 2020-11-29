def near(numOfCities, cities, xCoord, yCoord, numQueries, queries):
    central = zip(cities, xCoord, yCoord)

    cities = {}
    xHash = {}
    yHash = {}

    output = []

    for city, x, y in central:
        cities[city] = (x, y)
        xHash[x] = xHash.get(x, [])
        xHash[x].append(city)

        yHash[y] = yHash.get(y, [])
        yHash[y].append(city)

    for city in cities:
        curr_x = cities[city][0]
        curr_y = cities[city][1]

        shared_x = xHash.get(curr_x, [])
        shared_y = yHash.get(curr_y, [])

        min_distance = float("inf")
        town = None

        for val in shared_x:
            if val == city:
                continue

            else:
                nbr_coords = cities[val]
                dist = euc(cities[city], nbr_coords)

                if dist < min_distance:
                    town = val
                    min_distance = dist

                if dist == min_distance:
                    choose = [town, val]
                    choose.sort()
                    town = choose[0]

        for val in shared_y:
            if val == city:
                continue

            else:
                nbr_coords = cities[val]
                dist = euc(cities[city], nbr_coords)

                if dist < min_distance:
                    town = val
                    min_distance = dist

                if dist == min_distance:
                    choose = [town, val]
                    choose.sort()
                    town = choose[0]


        output.append(town)

    return output


def euc(tup1, tup2):
    # without sqroot, (x2-x1) ** 2 + (y2 - y1) ** 2
    return (tup1[0] - tup2[0]) ** 2 + (tup1[1] - tup2[1]) ** 2

numOfCities = 3

cities = ["c1", "c2","c3"]

xCoordinates = [3, 2, 1]

yCoordinates = [3, 2, 3]

numOfQueries = 3

queries = ["c1", "c2", "c3"]

print(near(numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries))