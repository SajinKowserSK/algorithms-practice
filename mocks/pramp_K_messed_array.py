import queue as q

def sort_k_messed_array(arr, k):
  # simple sort will be in O(n*log n) time but using
  # minheap or priority queue we can get O(n * log k) time

  # change = 0
  # [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
  # for x in range(0, len(arr)-1):
  # put item in priority queue (pq)
  # if the pq == k+1 (we have considered k+1 elements to the right)
  # arr[change]=pq.get()

  # in the end we have k elements in pq
  # so while pq is not empty
  # arr[change] = pq.get()
  # return arr

  pq = q.PriorityQueue()
  change_i = 0

  for x in range(0, len(arr)):
      pq.put(arr[x])

      if pq.qsize() == k+1:
          arr[change_i] = pq.get()
          change_i += 1

  while pq.qsize() != 0:
      arr[change_i] = pq.get()
      change_i += 1

  return arr


print(sort_k_messed_array([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2))