# given a low and high boundary of number range
# determine a winning sequence such that the sequence of array elements starting from the beginning are maximized

# brute force way - for every index from 1 to len(num)-1, place the highest val and then make left + right side decreasing
# get the max sum for the arrays
def winSeq(low, high, num):
    output = []

    # first we have to determine the appropriate index of the "peak" element so we can get the starting element
    # naturally we think its the highest - 1
    # however, to make sure we don't go beyond the range of low and high, we must pick the best
    # starting element such that we have enough elements on left and right side of the peak to satisfy the
    # high low constraints

    # first condition is to ensure peak doesn't exceed nums in return list range
    # second condition is to ensure

    # example: low = 2, high = 4, nums = 5
    # [3,4,3,2, X] -> doesn't work if you just put peak at 1
    # BUT if you optimize for peak position which is index 2
    # [2,3,4,3,2] -> WORKS

    peak = 1

    # if num - 1 (last indice) - peak greater than the range of numbers (high - low) we are a shortage of numbers
    # high - low instead of high - low + 1 bc one number is repeated anyway
    # keep updating peak
    while peak < num and num - 1 - peak > high - low:
        peak += 1

    val = high - peak

    for x in range(0, num):
        output.append(val)

        # ascending up until peak
        if x < peak:
            val += 1
        # descending after peak
        else:
            val -= 1

    if output[0] < low or output[-1] < low:
        return -1 # not possible to create winning sequence

    return output


print(winSeq(5, 51, 12))



