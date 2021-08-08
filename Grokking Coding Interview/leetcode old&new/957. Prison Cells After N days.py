class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        i = N
        seen = {}

        while i:

            check = tuple(cells)

            if check in seen:
                # we want to go close to 0 or see what's left until we reach 0
                # so we have to use mod to get a remainder
                # what we mod by should be the difference between
                # the last place we saw this occurence and where we are now AKA the cycle is everything in between (will repeat)

                i %= seen[check] - i

            seen[check] = i

            if i > 0:
                tmp = [0] * len(cells)

                for x in range(1, len(cells) - 1):
                    if cells[x - 1] == cells[x + 1]:
                        tmp[x] = 1

                    else:
                        tmp[x] = 0

                cells = tmp
                i = i - 1

        return cells
