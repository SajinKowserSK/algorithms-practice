# ANSWER
def twoStrings(arr):
    p = arr[0]
    pairs_counted = 0

    for x in range(1, len(arr)-1, 2):

        if pairs_counted == p:
            break

        string1 = arr[x]
        string2 = arr[x+1]

        unique_chars_1 = list(set(string1))
        unique_chars_2 = list(set(string2))
        seperate_uniques = unique_chars_1 + unique_chars_2


        summed_uniques = list(set(seperate_uniques))


        if len(summed_uniques) <  len(seperate_uniques):
            print("YES")

        else:
            print("NO")

        pairs_counted += 1


# TEST CASES
given_test_case = [2, 'hello', 'world', 'hi', 'world', 'ab', 'a'] # - > 'YES', 'NO'
custom_test_case = [2, 'abacus', 'abahus', 'boolin', 'coolin'] # - > 'YES', 'YES'
custom_test_case2 = [2, 'dawg', 'no', 'yuhhh', 'wta!'] # -> 'NO', 'NO'

twoStrings(given_test_case)
# twoStrings(custom_test_case)
# twoStrings(custom_test_case2)

# ALGORITHM ANALYSIS

# TIME COMPLEXITY
''' Time complexity is O(m + n) where m is length of string 1 and n is length of string 2 

    Not accounting for iterating through the input list, we have two strings at any given time, 
    string1 with size m and string2 with size n. The most expensive operation is when we 
    create a set with the total of unique characters from both strings. At worst case, this has 
    O(m + n) iterations.  
'''

# SPACE COMPLEXITY
'''Space complexity is also O(m + n) since at worst case, both strings have unique chars and 
    we create a list (summed_uniques) with all letters from each string.
'''


