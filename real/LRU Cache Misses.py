from collections import OrderedDict
# we use an ordered dict becuase it's easy to move to end, check for items in O(1) time
# ITEMS AT FRONT: LEAST RECENTLY USED, BACK: MOST RECENTLY USED
class LRUCache(OrderedDict):
    def __init__(self, capacity):
        # three fields are capacity: how much the cache can hold
        #                  misses: incremented every time something is requested & its not in cache
        #                  n: the number of items currently in cache, used to check if at capacity
        self.capacity = capacity
        self.misses = 0
        self.n = 0

    def hit(self, key): # also known as request method

        # check if the requested item is in the cache
        # if it is -> move it to the end as back = most recently used

        if key in self:
            self.move_to_end(key)

        # if it's not in the end then we can add it to the back
        # first increase misses because we made a request not in the cache
        # then add it to ordered dict and increase self.n by 1

        # check if n == capacity
        # if it is -> remove from the back and reduce n
        else:
            self.misses += 1
            self[key] = None
            self.n += 1

        if self.n > self.capacity:
            self.popitem(last=False)
            self.n -= 1


def lruCacheMisses(num, pages, maxCacheSize):
        lru_cache = LRUCache(maxCacheSize)
        for page in pages:
            lru_cache.hit(page)

        return lru_cache.misses

test = [1,2,1,3,1,2]
print(lruCacheMisses(len(test), test, 2))