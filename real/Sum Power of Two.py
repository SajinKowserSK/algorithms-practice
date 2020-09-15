# Input: arr[] = {3, 11, 14, 5, 13}
# Output: 2
# All valid pairs are (13, 3) and (11, 5) both sum up to 16 which is a power of 2.
# We could have used (3, 5) but by doing so maximum of 1 pair could only be formed.
# Therefore, (3, 5) is not optimal.
#
# Input: arr[] = {1, 2, 3}
# Output: 1
# 1 and 3 can be paired to form 4, which is a power of 2.

import math

from math import log2

pairs = []
a = [3, 3, 5, 11,14,5,13]

# create a dict with count of how many times a number appears since it can only
# be used once each appearance

count = dict.fromkeys(a, 0)
for x in range(len(a)):
    count[a[x]] += 1

for x in range(0, len(a)-1):
    sum = a[x]
    for y in range (x+1, len(a)):
        sum += a[y]
        if log2(sum) % 1 == 0:
            pairs.append((a[x],a[y]))

        sum -= a[y]

pairs = list(set(pairs))
t = pairs
t = sorted(t, key=lambda x: x[0] + x[1], reverse=True)

print("pairs sorted are", t)

removes = []
for x in range(0, len(t)):
    if count[t[x][0]] > 0 and count[t[x][1]] > 0:
        count[t[x][0]] -= 1
        count[t[x][1]] -= 1

    else:
        removes.append(t[x])


final = set(t) - set(removes)
final = list(final)
print(len(final))
print(final)
