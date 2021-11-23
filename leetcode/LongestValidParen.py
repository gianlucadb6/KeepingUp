"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        if s:
            max = 0
            leftParen = []
            leftParen.append(s[0])
            for i in range(1, len(s)):
                cur = s[i]
                prev = leftParen.pop()
                if prev == '(' and cur == ')':
                    length+=2
                else:
                    leftParen.append(s[i])
                    continue
                i+=1
                if i < len(s):
                    leftParen.append(s[i])
        return length
