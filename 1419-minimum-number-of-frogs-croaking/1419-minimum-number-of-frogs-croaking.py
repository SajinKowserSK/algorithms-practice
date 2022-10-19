class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        '''

        everytime we encounter a char, we will decrement the one before it by 1 and increase its value by 1 
        at the end of every iteration we will take the value of the sum of the array 

        c: 0 
        r: 0
        o: 0
        a: 0
        k: 0
        '''
        
        indices = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        tmp = [0, 0, 0, 0]
        count = 0 

        for char in croakOfFrogs:
            index = indices[char]

            if tmp[index-1] == 0 and char != 'c': # not valid combo if the one before is a 0 and it's not a c
                return -1

            if char != 'c':
                tmp[index-1] -= 1

            if index != 4:
                tmp[index] += 1

            count = max(count, sum(tmp))

        return count if sum(tmp) == 0 else -1

