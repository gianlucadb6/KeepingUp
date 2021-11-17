"""

"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        for pre in wordDict:
            if s.startswith(pre):
                wordDict.remove(pre)
                s = s[len(pre)-1:]
        if not wordDict:
            return True
        else:
            return False

#need to check the rest of the string, not just once for each word in the dictionary
