t = [2,7,8,5,1,6,3,9,4]


def minimalPeaks(arr):
    removes = []
    while len(arr) > 1:
        peaks = []
        for x in range(len(arr)):
            if x == 0:
                if arr[x] > arr[x+1]:
                    peaks.append(arr[x])

            elif x == len(arr) - 1:
                if arr[x] > arr[x-1]:
                    peaks.append(arr[x])

            else:
                if arr[x] > arr[x-1] and arr[x] > arr[x+1]:
                    peaks.append(arr[x])

        min_peak = min(peaks)
        removes.append(min_peak)
        arr.remove(min_peak)


    removes.append(arr[0])
    print(removes)
    return None

minimalPeaks(t)