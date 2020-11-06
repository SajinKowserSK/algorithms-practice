def reverse(n):

    string = str(n)
    new = ""
    last = 0
    if len(string) % 2 == 0:
        for x in range(len(string)-1, -1, -2):
            new = "" + string[last:x]
            last = x


    else:
        for x in range(len(string)-2, -1, -2):
            new = "" + string[last:x]
            last = x

    return int(string)

print(reverse(123456))



