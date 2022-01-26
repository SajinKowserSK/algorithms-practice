
def find(memory, size):
    s = memory.index(0)
    j = s

    while j < len(memory)-1:

        if (j-s+1) == size:
            break

        j += 1
        if memory[j] == 1:
            s = memory.index(0, j)
            j = s

    print((s,j))

memory = [0,1,0,0,0,1,0]
find(memory, 3)

