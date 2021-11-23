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
        max = 0
        if s:
            leftParen = []
            for i in range(len(s)):
                cur = s[i]
                if cur == ')':
                    if leftParen:
                        prev = leftParen.pop()
                        if prev:
                            length+=2
                    else:
                        if length >= max:
                            max = length
                        length = 0        
                else:
                    leftParen.append(cur)
                    
                if length >= max:
                    max = length
        return max
