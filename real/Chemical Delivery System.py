class PairInt:
    def __init__(self,first,second):
        self.first = first
        self.second = second

def getMarkings(numOrders, requirements, flaskTypes, totalMarks, markings):
    ret = -1

    flask_dict = {}

    for pair in markings:
        if pair.first not in flask_dict:
            flask_dict[pair.first] = [pair.second]

        else:
            flask_dict[pair.first].append(pair.second)

    min_waste = None

    for key in flask_dict:

        flask_dict[key].sort()
        wasted = 0
        found = True
        markings = flask_dict[key]

        for req in requirements:
            if markings[-1] < req:
                found = False

            for mark in markings:
                if mark < req:
                    continue

                else:
                    sum = mark - req
                    wasted += sum
                    break

        if found == False:
            continue

        else: # found is true
            if min_waste is None or wasted < min_waste:
                min_waste = wasted
                ret = key

    return ret


markings = [PairInt(0,3),
            PairInt(0,5),
            PairInt(0,7),
            PairInt(1,6),
            PairInt(1,8),
            PairInt(1,9),
            PairInt(2,3),
            PairInt(2,5),
            PairInt(2,6)]

print(getMarkings(4,[4,6,6,7],3,9,markings))