#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'vanity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING_ARRAY numbers
#

def vanity(codes, numbers):
    # first we will create a map with each letter's pairing to the phone pad
    alpha_dict = {2: ["a", "b", "c"],
                  3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"],
                  7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}

    new = {}
    for key in alpha_dict:
        for letters in alpha_dict[key]:
            letters = letters.upper()
            new[letters] = str(key)

    alpha_dict = new

    # now we translate the codes to it's number alternative
    number_codes = []
    for code in codes:
        translated = ""
        for x in range(0, len(code)):
            translated += alpha_dict[code[x]]

        number_codes.append(translated)

    # now we iterate through the numbers and see if the code is a substring in any of the numbers
    result = []
    for code in number_codes:
        for number in numbers:

            # we have to mutate the string by stripping the + away from the start so we can append it as a number
            # this step is essentail to output a sorted array
            number = number[1::]
            number = int(number)

            if code in str(number) and number not in result:
                result.append(number)

    result.sort()

    for x in range(0, len(result)):
        number = "+" + str(result[x])
        result[x] = number

    return result


if __name__ == '__main__':