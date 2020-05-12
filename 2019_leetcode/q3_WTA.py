# Given a list of strings representing your own travel preferences
# And a list of lists with your friends travel preferences, return the index of the list with most in common with yours


def TravelCompatability(mylist, friendlist):

    index = -1

    for places1 in mylist:

        same = 0
        for friend in friendlist:
            for places2 in friend:
                if places1 == places2:
                    same = same+1

            if same > 0 and same > index:
                index = friendlist.index(friend)

    return index


print(TravelCompatability(["YYZ", "JFK", "SFO"], [["YTU", "YPZ"], ["SAO", "BFS", "JWK"]]))


