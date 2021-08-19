def find_subsets(nums):
    subsets = []
    subsets.append([])
    for num in nums:
        for x in range(len(subsets)):
            elem = subsets[x]
            print(elem)
            add = elem.copy()
            add.append(num)
            subsets.append(add)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
