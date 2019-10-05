# Given a string
# Return longest substring with most alpahbetical characters

def longestAlphabeticalSubstring(s):
    """Given a string return the longest substring that is in alphabetical string."""

    alphabeticalSubstrings = []
    for x in range(len(s)):
        for y in range(len(s),x,-1):
            if isAlphabetical(s[x:y]):
                alphabeticalSubstrings.append(s[x:y])
    longestSubstring = ''
    for strings in alphabeticalSubstrings:
        if len(strings) >= len(longestSubstring):
            longestSubstring = strings

    return longestSubstring


def isAlphabetical(string):
    '""Return if a string is in alphabetical format.'

    for x in range(len(string)-1):
        if ord(string[x]) > ord(string[x+1]):
            return False

    return True


print(longestAlphabeticalSubstring('abfcj'))



