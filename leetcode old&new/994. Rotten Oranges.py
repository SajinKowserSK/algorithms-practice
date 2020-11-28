class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count fresh oranges
        # count and add to q any rotten oranges (as points)
        # after adding all the rotten oranges from minute 0, add a None to the q
        # the None will track level

        # while q is not empty
        # pop from queue and then check each of the directions for any unrotten (1)
        # mark that as rotten and add it to the queue
        # we need to also track level
        # so if while popping from q, encounter a None, immediately add another None to the end of the queue
        # increase the minutes or depth
        # if queue start == queue end (both None) then break the whole thing

        # at the end, return minutes if fresh == 0 otherwise return -1

        fresh = 0
        rot_q = []
        minute = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == 2:
                    entry = (row, col)
                    rot_q.append(entry)

                elif grid[row][col] == 1:
                    fresh += 1

        ROW = len(grid)
        COL = len(grid[0])

        rot_q.append(None)  # None marks the end of a bfs level

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

        print(rot_q)
        while rot_q:
            popped = rot_q.pop(0)

            if popped == None:
                if rot_q:
                    minute += 1
                    rot_q.append(None)


            else:

                for d in directions:

                    new_row = popped[0] + d[0]
                    new_col = popped[1] + d[1]

                    if new_row >= 0 and new_row < ROW and new_col >= 0 and new_col < COL:

                        # print("p", popped, "d", d, "new_coord", (new_row, new_col), "new_val", grid[new_row][new_col])

                        nbr = grid[new_row][new_col]
                        entry = (new_row, new_col)

                        if nbr == 1:
                            grid[new_row][new_col] = 2
                            fresh -= 1

                            rot_q.append(entry)

        print("grid", grid)
        return minute if fresh == 0 else -1





