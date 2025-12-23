from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        count_s1 = Counter(s1)
        window = Counter(s2[:len1])

        if window == count_s1:
            return True

        for i in range(len1, len2):
            # add new character to the window
            window[s2[i]] += 1

            # remove the character going out of the window
            left_char = s2[i - len1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

            if window == count_s1:
                return True

        return False



'''
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''