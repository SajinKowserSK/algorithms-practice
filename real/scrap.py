# practice soln 1 completed on lc

# practice soln 2 completed on lc

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

            # sort intervals by starting time
        intervals = sorted(intervals)

        # start with 1 room and put first meeting in there
        room_dict = {}
        rooms = 1
        room_dict[rooms] = intervals[0]

        # for all times up until the second last one
        for x in range(0, len(intervals) - 1):

            # check current time and adjacent time
            curr = intervals[x]
            nex = intervals[x + 1]

            # if next meetings starting time is before the current one ends , need a room
            if nex[0] < curr[1]:
                need_room = True

                # check if others are free
                for y in range(1, rooms + 1):

                    # if the start time of next is after a room's end time or at an end time of someone already in the room
                    if nex[0] >= room_dict[y][1]:
                        room_dict[y] = nex

                        # we no longer need room
                        need_room = False
                        break

                # if none are free, add a new room and put the time in there
                if need_room:
                    rooms += 1
                    room_dict[rooms] = nex

            else:
                room_dict[rooms] = nex

        return rooms
