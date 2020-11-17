def earliestTime(numBuildings, buildingopenTime, offloadTime):
    buildingopenTime.sort()
    offloadTime.sort(reverse=True)

    earliest = None
    start = 0

    for x in range(0, len(offloadTime)):
        curr_offload = offloadTime[x]

        if x != 0 and x % 4 == 0:
            start += 1


        if earliest is None:
            earliest = buildingopenTime[start] + curr_offload

        else:
            curr_sum = buildingopenTime[start] + curr_offload

            if curr_sum == 18:
                print(start, curr_offload)

            earliest = max(earliest, buildingopenTime[start] + curr_offload)


    return earliest

test = [8,10]
test_offload = [2,2,3,1,8,7,4,5]
print(earliestTime(len(test), test, test_offload))
