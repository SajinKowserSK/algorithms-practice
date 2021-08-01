def insert(intervals, new_interval):
  merged = []

  i = 0

  # auto adding all the ones whose ending time is before the added intervals starting time
  while i < len(intervals) and intervals[i][1] < new_interval[0]:
      merged.append(intervals[i])
      i += 1


  # we know that our curr intervals[i] end time will be after the added interval's start time
  # now to know that it overlapping, the start time for it has to be before or at the end time for the new interval
  while i < len(intervals) and intervals[i][0] <= new_interval[1]:
      new_interval[0] = min(intervals[i][0], new_interval[0])
      new_interval[1] = max(intervals[i][1], new_interval[1])
      i += 1

  # no more overlappings so we can add the merged interval
  merged.append(new_interval)


  # add remaining items
  for x in range(i, len(intervals)):
      merged.append(intervals[x])


  return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
#
#
# Intervals after inserting the new interval: [[1, 3], [4, 7], [8, 12]]
# Intervals after inserting the new interval: [[1, 3], [4, 12]]
# Intervals after inserting the new interval: [[1, 4], [5, 7]]