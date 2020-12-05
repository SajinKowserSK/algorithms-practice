# make a flask dict with {flaskIndex: markings: int}
# initialize a min waste to float("inf) or none, ret to -1
# iterate through each flask key
# sort flask[key]
# iterate through each requirement in requirements
# if the req > flask[key]'s last elem, go to the next flask type
# continously update min_waste and only update the global variable if min waste is less than the global, keep track of ret too

class PairInt:
    def __init__(self,first,second):
        self.first = first
        self.second = second

def getMarkings(numOrders, requirements, flaskTypes, totalMarks, markings):
    ret = -1

    flask_dict = {}
    # make a dict of {flaskType: [markings:int]}
    for pair in markings:
        if pair.first not in flask_dict:
            flask_dict[pair.first] = [pair.second]

        else:
            flask_dict[pair.first].append(pair.second)

    min_waste = None

    for key in flask_dict:

        # sort them for easy comparability (also need to check if max capacity <= max marking)
        # also want the first compatable marking, sorting makes this easier
        flask_dict[key].sort()
        wasted = 0
        found = True
        markings = flask_dict[key]

        for req in requirements:
            # no need to continue iterating if max isn't bigger than requirement
            if markings[-1] < req:
                found = False
                break

            for mark in markings:
                if mark > req:
                    sum = mark - req
                    wasted += sum
                    break

        if found == False:
            continue

        else: # found is true
            if min_waste is None or wasted < min_waste: # only update if min waste is none or the current waste is less than prev
                # second condition prevents providing a later index w same waste
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