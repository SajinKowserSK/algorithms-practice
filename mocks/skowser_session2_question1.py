# PSEUDOCODE
'''iterate for number of shifts
take from front
add to back '''

# ANSWER
def left_rotation(n, d, arr):

    if n == 0:
        return []

    # not really necessary since there's a constraint of d < n
    # but to prevent long TC
    d = d % n

    for x in range(0, d):
        front = arr.pop(0)
        arr.append(front)

    return arr

# TEST CASES
given_test_case = [1,2,3,4,5]
custom_test_case = [1,2]
custom_test_case_2 = [5]

print(left_rotation(len(given_test_case), 4, given_test_case)) # -> [5, 1, 2, 3, 4]
print(left_rotation(len(custom_test_case), 1, custom_test_case)) # -> [2, 1]
print(left_rotation(len(custom_test_case_2), 0, custom_test_case_2)) #-> [5, 8, 3]

# ALGORITHM ANALYSIS

## TIME COMPLEXITY
'''the time complexity will be O(n) since we iterate at most n elements in array 
this is ensured even when d > n by doing d % n 
the python pop function from the front as well as append to back of list are both constant time opertions'''

## SPACE COMPLEXITY
''' the space complexity will be O(1) since we did not use any auxilliary space'''


