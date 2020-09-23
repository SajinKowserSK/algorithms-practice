test = "1n the first video, we can observe that the male (left) is likely analytical. He asks questions to make a well-informed decision while not committing early-on . 2n the first video, we can observe that the male (left) is likely analytical. He asks questions to make a well-informed decision while not committing early-on . 3n the first video, we can observe that the male (left) is likely analytical. He asks questions to make a well-informed decision while not committing early-on. JIBBERISH"

total = len(test) // 160
if len(test) % 160 != 0:
    total += 1

lst = []

sect = 1
counter = 0

for x in range(160, len(test), 160):
    extra = "("+str(sect)+"/"+str(total)+")"
    division = test[counter:x] + extra
    lst.append(division)
    print(len(test[counter:x]), division)

    sect += 1
    counter += 160


extra = "(" + str(sect) + "/" + str(total) + ")"
division = test[counter::] + extra
lst.append(division)
print(len(test[counter::]), division)
#
# for section in lst:
#     print(section, "\n")