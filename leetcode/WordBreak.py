"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        while s:
            found = False
            for pre in wordDict:
                if s.__contains__(pre):
                    s = s.replace(pre, "")
                    found = True
                    break
            if not found:
                return False
        return True

#i think i may be confused, but works for a few cases. one of the cases i am getting wrong seems like one of the examples in the description and this code should pass that case.
