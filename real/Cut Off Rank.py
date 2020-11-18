def cutOff(scores, cutOff):

    scores.sort(reverse=True)
    scoreMap = {}
    counter = 0

    for x in range(0, len(scores)):
        curr = scores[x]

        if curr not in scoreMap:
            rank = x + 1
            scoreMap[curr] = rank

        else:
            rank = scoreMap[curr]


        if rank <= cutOff:
            counter += 1

    return counter

test = [100,25,50,50]
test2 = [2,2,3,4,5]
print(cutOff(test, 2))