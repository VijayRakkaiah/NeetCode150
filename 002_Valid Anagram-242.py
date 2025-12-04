class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for j in t:
            if j not in d:
                return False
            elif d[j] > 1:
                d[j] -= 1
            else:
                del d[j]
        
        if d == {}:
            return True
        else:
            return False
            

'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

'''