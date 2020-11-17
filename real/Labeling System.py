import heapq

def invalid(lst, charLimit):
    for x in range(len(lst)-1, -1+charLimit, -1):
        subset = lst[x-charLimit:x+1]

        if len(set(subset)) == 1:
            return True

    return False

def swap(lst, start, end):
    tmp = lst[start]
    lst[start] = lst[end]
    lst[end] = tmp

def fix(str, charLimit):
    lst = list(str)

    stop = 0
    start = len(str)-1
    end = len(str)-2

    while invalid(lst, charLimit) and stop < 6:

        # first identify where the invalid string is
        # go from the start of the invalid sub string
        # swap the the left of the start
        # rerun the loop

        for x in range(len(lst)-1, -1+charLimit, -1):
            subset = lst[x - charLimit:x + 1]

            if len(set(subset)) == 1:
                start = x - charLimit

        adjacent = start - 1
        tmp = lst[adjacent]
        lst[adjacent] = lst[start]
        lst[start] = tmp

    final = ""
    return final.join(lst)


def label(originalLabel, charLimit):
    lst = []

    for x in range(0, len(originalLabel)):
        curr = originalLabel[x]
        lst.append((ord(curr)*-1, curr))

    strk = 0

    final = ""
    heapq.heapify(lst)


    while lst:

        popped = heapq.heappop(lst) # gives highest order

        if len(final) == 0 or final[-1] != popped[1]:
            final += popped[1]
            strk = 1

        elif final[-1] == popped[1]:

            if strk < charLimit:
                final += popped[-1]
                strk += 1

            else: # strk limit reached
                # we need to find the next greatest


                broken = False
                addBack = []
                addBack.append(popped)

                if len(lst) == 0:
                    broken = True

                while lst:

                    vals = [x[1] for x in lst]
                    if len(set(vals)) == 1:
                        broken = True
                        break

                    new_popped = heapq.heappop(lst)
                    if new_popped[1] != final[-1]:
                        break

                    else:
                        addBack.append(new_popped)

                while addBack:
                    heapq.heappush(lst, addBack[0])
                    addBack.pop(0)

                if broken:
                    for elem in lst:
                        final+=elem[1]
                    final = fix(final, charLimit)
                    return final

                else:
                    final += new_popped[1]
                    strk = 1

    return final


fin = label("bcccaaa", 1)
print(fin)