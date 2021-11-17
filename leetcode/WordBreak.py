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
            for pre in wordDict:
                if s.__contains__(pre):
                    s = s.replace(pre, "")
                    break
                else:
                    return False
        return True

#i think this should work, i am missing something simple
