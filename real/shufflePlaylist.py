from random import random
from collections import deque


class playlist:
    def __init__(self, lst, skipOrder):
        self.lst = lst
        self.length = len(lst)
        self.skipOrder = skipOrder
        self.played = 0
        self.waitList = deque()

    def getRandomSong(self):
        # we waited an iteration of the cooldown period
        # add the oldest item put on the wait list

        if (self.played - 1) >= self.skipOrder and self.waitList:
            toAdd = self.waitList.popleft()
            self.lst.append(toAdd)
            self.length += 1

        # play a random index of the song
        random_index = int(random() * 100) % self.length
        play = self.lst[random_index]  # random song to play

        tmp = self.lst[-1]
        self.lst[-1] = self.lst[random_index]
        self.lst[random_index] = tmp
        del self.lst[-1]
        self.length -= 1

        # add to wait list & increment songs played
        self.waitList.append(play)

        self.played += 1
        return play


print(
    "QUESTION: Random music shuffle question. Given a list of songs and a skip order like songs = [A,B,C,D], skipOrder = 2. If a song is played once, it cannot be back in the shuffling list till skipOrder is done. Ex: If A is played first and then A cannot be back in the list until next 2 iterations.")

print("\n")

obj = playlist(['A', 'B', 'C', 'D'], 2)
for x in range(10):
    print("Playing: ", obj.getRandomSong(),
          "UpNext: ", obj.lst,
          "Cooldown: ", list(obj.waitList),
          "Played: ", obj.played)
