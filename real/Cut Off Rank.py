
# TC -> O(nlogn) SC -> O(n)
def cutOff(scores, cutOff):

    scores.sort(reverse=True) # high scores
    scoreMap = {}
    counter = 0

    for x in range(0, len(scores)):
        curr = scores[x]

        # updates rank according to their index position
        if curr not in scoreMap:
            rank = x + 1
            scoreMap[curr] = rank
        # if it's already in it, get the first rank occurence
        else:
            rank = scoreMap[curr]

        # increment if rank is below or equal to cutoff
        if rank <= cutOff:
            counter += 1

    return counter

test = [100,25,50,50]
test2 = [2,2,3,4,5]
print(cutOff(test, 2))