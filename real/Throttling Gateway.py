
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



def numDropped2(nums, requestTime):
    dropped = 0

    for x in range(3, len(requestTime)): # starting from 3 for eligibility with condition 1
        # CONDITION 1: CAN'T HAVE MORE THAN 3 TRANSACTIONS PER SECOND
        # transactions at any 1s can't exceed 3
        # we can see our second now vs where it was 4 elements ago -> if it's the same then thats 4 transactions and drop

        if requestTime[x] == requestTime[x-3]:
            dropped += 1

        # CONDITION 2: CAN'T HAVE > 20 TRANSACTIONS IN 10S
        # start at 21st element (i = 20) because 20th element is allowed under "can have 20 transactions in 10s"
        # we want to check if the 21st element and 1st element are within 10s, if they are then drop.
        # NOT <= 10 because 0 counts as "same seconds"
        elif x > 19 and requestTime[x] - requestTime[x-20] < 10:
            dropped += 1

        elif x > 59 and requestTime[x] - requestTime[x-60] < 60:
            dropped += 1
    return dropped

test = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
numDropped(len(test), test)
print(numDropped2(len(test), test))