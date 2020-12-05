# building opening time is the time all (4) docks of the building opens
# each building can take only 4 deliveries
# we want to get the earliest time all buildings are ready to go

# assuming building open time is in chronological order, we can sort offload time delivery in decreasing order
# now we can assign the first 4 to the earliest time then the next 4 to the second earliest time, all the way to
# the nth earliest time
def earliestTime(numBuildings, buildingopenTime, offloadTime):
    buildingopenTime.sort()
    offloadTime.sort(reverse=True) # do this bc we want to match longest deliv times w earliest times to minimize length

    earliest = None
    start = 0

    for x in range(0, len(offloadTime)):
        curr_offload = offloadTime[x]

        # this means after 4 packing 4 deliveries, move the "start" index to the next building
        # since the last building's 4 docks are now full
        if x != 0 and x % 4 == 0:
            start += 1

        # if earliest is none, update it to the current off load t ime
        if earliest is None:
            earliest = buildingopenTime[start] + curr_offload

        # otherwise, we know take the most of the current building time and current value of earliest
        else:
            curr_sum = buildingopenTime[start] + curr_offload
            earliest = max(earliest, curr_sum)


    return earliest

test = [8,10]
test_offload = [2,2,3,1,8,7,4,5]
print(earliestTime(len(test), test, test_offload))
