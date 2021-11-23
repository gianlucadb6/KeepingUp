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
        leftParen = []
        for paren in s:
            if leftParen:
                if leftParen.pop() == '(':
                    if paren == ')':
                        length+=1
                        continue
            elif paren == '(':
                leftParen.append(s)
                continue
            leftParen = []
        return length
