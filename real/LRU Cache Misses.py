class dll:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = dll(-1, -1)  # dummy node for refernece to start (self.head.next is real head)
        self.tail = self.head
        # ref key: int value: the Node
        self.hmap = {}
        self.capacity = capacity
        self.n = 0

    def get(self, key: int) -> int:
        if key in self.hmap:
            # need to move the key to the end
            # need to return the value

            node = self.hmap[key]
            val = node.val

            if node.next:  # TEST AFTER SUCCESS
                # update neighbors
                node.prev.next = node.next
                node.next.prev = node.prev

                # move node to tail's end
                self.tail.next = node
                node.prev = self.tail

                # update tail
                node.next = None
                self.tail = node

            return val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            # update the key

            node = self.hmap[key]
            node.val = value

            # move to end of dll
            if node.next:  # TEST AFTER SUCCESS
                # update neighbors
                node.prev.next = node.next
                node.next.prev = node.prev

                # move node to tail's end
                self.tail.next = node
                node.prev = self.tail

                # update tail
                node.next = None
                self.tail = node

        else:

            toAdd = dll(key, value)
            self.hmap[key] = toAdd

            self.tail.next = toAdd
            toAdd.prev = self.tail
            toAdd.next = None
            self.tail = toAdd

            self.n += 1

            if self.n > self.capacity:
                # evict least recently used, so the head
                # our heads a dummy so real head is self.head.next
                toRemove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

                del self.hmap[toRemove.key]
                self.n -= 1

            # Your LRUCache object will be instantiated and called as such:


# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



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