class Solution:

    # for any two a, b
    # if a % 60 == 0 then b % 60 also has to be 0
    # however if a % 60 != 0 then (a % 60 + b % 60) % 60 == 0 or 60 which reduces to 0
    # isolate for b % 60 = 60 - a % 60
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        map1 = collections.defaultdict(int)

        rems = {}

        count = 0

        for x in range(0, len(time)):
            elem = time[x]

            og_need = elem % 60
            need = elem % 60

            if need == 0:
                count += map1[need]

            else:
                need = 60 - elem % 60

                if need in map1:
                    count += map1[need]

            map1[elem % 60] += 1

        return count


