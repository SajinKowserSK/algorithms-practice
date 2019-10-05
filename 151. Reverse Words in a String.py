'''Title : 151. Reverse Words in a String
Difficulty = Medium
Description: Given an input string, reverse the string word by word. '''

class solution(object):
    def reverseWords(self, s):
        rString = ""
        if len(s) >0:
            list1 = s.split()
            #rString = ""

            for x in range (len(list1)-1, -1, -1):
                rString = rString +" " +list1[x]

        return rString.lstrip()


