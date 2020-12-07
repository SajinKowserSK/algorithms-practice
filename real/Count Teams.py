def count(num, skills, minEmp, minLevel, maxLevel):
    if len(skills) == 0:
        return 0

    # get eligibles
    eligible = 0
    for x in range(0, len(skills)):
        if minLevel <= skills[x] <= maxLevel:
            eligible += 1

    # create factorial tables
    factorialTable = {}
    createFTable(num, factorialTable)

    #
    total = 0

    # combination formula -> for total we want to add
    # CHOOSE FORMULA (n!/(n-k)! * k!)
    # from minAssosciates to eligible inclusive


    for x in range(minAssociates, eligible+1):
        total += factorialTable[eligible] / factorialTable[x] * factorialTable[eligible - x]

    print(total)
    return int(total)

def createFTable(num, table):
        if num == 0:
            table[num] = 1

        else:
            createFTable(num-1, table)
            table[num] = num * table[num-1]
'''
{3: 6
2: 2
1: 1
0: 1
'''

def choose(n, k, table):
    return (table[n]) / ((table[n-k]) * (table[k]))


num = 6
skills = [12, 4, 6, 13, 5, 10]
minAssociates = 3
minLevel = 4
maxLevel = 10

print(count(num, skills, minAssociates, minLevel, maxLevel))