class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in d.keys():
                stack.append(d[i])
            else:
                if stack == []:
                    return False
                elif i == stack[-1]:
                    stack.pop()
                else:
                    return False

        if stack == []:
            return True

        else:
            return False



'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
'''