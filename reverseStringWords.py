
def reverseWords(givenStr):
    lst = givenStr.split()
    new = ""
    for x in range (len(lst)-1, -1, -1):
        curr = lst[x]
        new = new + " " + curr

    return new


print(reverseWords("I am sajin"))

