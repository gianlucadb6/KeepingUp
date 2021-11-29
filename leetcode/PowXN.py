"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return x*self.myPow(x,n-1)
