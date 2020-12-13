def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

    key = keysPressed[0]
    longestRelease = releaseTimes[0]
    for i in range(1, len(releaseTimes)):
        if longestRelease < releaseTimes[i] - releaseTimes[i-1]:
            longestRelease = releaseTimes[i] - releaseTimes[i-1]
            key = keysPressed[i]
        elif longestRelease == releaseTimes[i] - releaseTimes[i-1] and ord(key) < ord(keysPressed[i]):
            key = keysPressed[i]
    return key

def slow_key(arr):
    longest = [arr[0][0], arr[0][1]]

    for x in range(1, len(arr)):

        curr = arr[x]
        prev = arr[x-1]

        diff = curr[1] - prev[1]

        if diff > longest[1]:
            longest[1] = diff
            longest[0] = curr[0]

    print(longest[1])
    return chr(97 + longest[0])


print(slow_key([(0,2), (1,5), (0, 9), (2,15)]))


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowest = float('-inf')
        slowest_char = None
        prev = 0

        for x in range(0, len(releaseTimes)):
            curr_time = releaseTimes[x]
            diff = curr_time - prev

            if diff > slowest:
                slowest = diff
                slowest_char = keysPressed[x]

            elif diff == slowest: # still replace if lexigraphically larger"
                if ord(keysPressed[x]) > ord(slowest_char):
                    slowest_char = keysPressed[x]

            prev = curr_time

        return slowest_char

