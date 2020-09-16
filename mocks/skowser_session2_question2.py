# PSEUDOCODE
'''get letters in string
form pairs
for pair in pairs
see the string with just the pairs
check if valid string
get length of string
return highest length'''

# ANSWER
def alternate(n, string):
    string = string.lower()
    pairs = helper_get_pairs(string)
    max = 0


    for pair in pairs:
        alt_str = ""
        for char in string:
            if char == pair[0] or char == pair[1]:
                alt_str += char

        if helper_check_valid(alt_str) and len(alt_str) > max:
            max = len(alt_str)
    return max


def helper_check_valid(string):

    if len(string) == 0 or len(string) == 1 or len(string) == 2 and string[0] == string[1]:
        return False

    for x in range(0, len(string)-2):
        if string[x] != string[x+2] or string[x] == string[x+1]:
            return False

    return True

def helper_get_pairs(string):
    unique_chars = list(set(string))

    pairs = []
    for x in range(0, len(unique_chars) - 1):
        for y in range(x + 1, len(unique_chars)):
            pairs.append([unique_chars[x], unique_chars[y]])

    return pairs

print(len(helper_get_pairs("abcd")))
# TEST CASES
given_test_case = "beabeefeab" # -> 5
custom_test_case = "abbcdabbc" # -> 4
custom_test_case2 = "aaaaa" # -> 0

print(alternate(10, given_test_case))
print(alternate(len(custom_test_case), custom_test_case))
print(alternate(len(custom_test_case2), custom_test_case2))

# ALGORITHM ANALYSIS

## TIME COMPLEXITY
''' The time complexity is O(n) or O(a^2 * n) at worst where "a" (a constant) 
    is the number of letters in the alphabet (pair function). The pair function is O(a^2) since at worst, 
    
    PAIR FUNCTION - O(1) or O(a^2)
    The string can have 26 unique letters and we look for every unique pair. However since at worse this would 
    yield 25+24+23...+1 operations (a constant) it may also be constant or O(1) time. 
    
    CREATING ALTERNATE STRING WITH EACH PAIR OF LETTERS - O(n) 
    Since we don't know the max length of string (unlike pairs where we did know the max number), 
    this will iterate through n items in the string so O(n) time 
    
    CHECK VALID STRING - O(n) 
    We iterate through each item in the string up until n-2 so O(n-2) or O(n) time.
    Since this happens in the iteration of pair loops ( O(1) or O(a^2) time complexity), 
    we get a total time complexity of O(n) if we consider a^2 to be constant and 
    O(n * a^2) if we do not.
'''
## SPACE COMPLEXITY
''' At worst, we create an alt_stirng of all characters, so O(n) space'''