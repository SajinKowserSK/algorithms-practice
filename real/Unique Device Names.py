# keep a stringMap of {string: occurences:int} so you can name it as name = string+str(stringMap[string])
def uniqDev(arr):
    strmap = {}

    new_arr = []
    for elem in arr:
        if elem not in strmap:
            strmap[elem] = 1
            new_arr.append(elem)

        else:
            new_str = elem + str(strmap[elem])
            strmap[elem] += 1
            new_arr.append(new_str)

    return new_arr

test = ["switch", "tv", "switch", "tv", "switch", "tv"]
print(uniqDev(test))

