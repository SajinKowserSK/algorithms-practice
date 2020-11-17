
def numDropped(nums, requestTime):
    dropped = 0
    for x in range(3, nums):

        # since it's in consec order, if sliding window of 3 in middle have both sides being same, > 3 requests per sec
        if requestTime[x] == requestTime[x-3]:
            dropped += 1
            continue # need to add to remove double counting

        # after 20 requests, we need to check if the request 20 requests ago is within 10 seconds
        if x > 19 and requestTime[x] - requestTime[x-20] < 10:
            dropped += 1
            continue

        # after 60 requests, we need to check if the request 60 requests ago is within 60 seconds
        if x > 59 and requestTime[x] - requestTime[x-60] < 60:
            dropped += 1
            continue

    print(dropped)
    return dropped




test = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
numDropped(len(test), test)