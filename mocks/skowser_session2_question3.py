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
twoStrings(custom_test_case)
twoStrings(custom_test_case2)

# ALGORITHM ANALYSIS

# TIME COMPLEXITY
''' Time complexity is O(n) and space complexity is O(1) 
    
    The most expensive operation is when unique_chars_1 and unique_chars_2 are created (list of unique chars 
    in each substring). To do this, all chars of string 1 and string 2 have to be iterated through which has either
    m or n items. The one with more chars is the more time-expensive operation so O(n). 
    
   len(seperate_uniques) would not be O(n + m) time since we know the chars are asci[a-z] and the list contains
   unique chars or alphabet letters only so thats O(26) -> O(1) time.
'''

# SPACE COMPLEXITY
'''Space complexity is O(1) in the worst case since at most we can have a list of 26 unique letters 
    (not more since the list adds sets made from lower-case alhabet letters together)
'''


