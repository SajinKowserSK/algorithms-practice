def reverse (x):
    strX = str(x)
    valid = ["1","2", "3", "4", "5", "6", "7", "8", "9", "0"]
    retS = ""
    special = ""

    if strX[0] not in valid:
        special = strX[0]
        strX = strX.replace(special,"")

    for y in range (len(strX)-1, -1, -1):
        retS = retS + strX[y]

    while retS[0] == "0":
        retS = retS[1:]

    retS = special+retS
    return retS

print(reverse(12000))
