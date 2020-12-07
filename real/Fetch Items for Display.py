def fetchItemsToDisplay(numOfItems, items, sortParam, sortOrder, itemsPerPage, pageNumber):
    main = []
    for item in items:
        vals = items[item] # first is relevance and second is price
        relevance = vals[0]
        price = vals[1]

        main.append([item, relevance, price])

    main.sort(key = lambda x: x[sortParam])

    if sortOrder == 1:
        main.sort(key = lambda x: x[sortParam], reverse=True)

    # now we have a whole master page with all items sorted, need to go to specific page
    # start at pg 0, go to page n (so up till n+1), SKIP COUNT by # Items on Page
    # also update start += skipCount
    start = 0
    for pageNum in range(0, pageNumber+1, itemsPerPage):
        start += itemsPerPage

    return [x[0] for x in main[start:start+itemsPerPage]]


map1 = {"item": (10, 15), "item2": (3,4), "item3": (17, 8), "item4": (20, 6), "item5": (22, 19)}
print(fetchItemsToDisplay(3, map1, 1, 0, 2, 2))