def count(num, skills, minEmp, minLevel, maxLevel):
    if len(skills) == 0:
        return 0

    eligible = 0
    for x in range(0, len(skills)):
        if minLevel <= skills[x] <= maxLevel:
            print(skills[x])
            eligible += 1


    factorialTable = {}
    createFTable(num, factorialTable)

    possible_teams = choose(eligible, minEmp, factorialTable)
    print(eligible, factorialTable)
    return possible_teams

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