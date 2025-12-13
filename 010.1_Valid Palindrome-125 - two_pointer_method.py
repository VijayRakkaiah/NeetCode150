class Solution:
    @staticmethod
    def isAlphaNumeric(c):
        return ('0' <= c <= '9') or ('a' <= c <= 'z') or ('A' <= c <= 'Z')

    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        s = s.lower()

        while l < r:
            while not self.isAlphaNumeric(s[l]) and l < r:
                l += 1
            while not self.isAlphaNumeric(s[r]) and r > l:
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True


'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''