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
        elif n == -1:
            return 1/x
        else:
            if n > 0:
                return self.myPow(x, n//2)*self.myPow(x,n//2) if n%2==0 else self.myPow(x, n//2)*self.myPow(x,n//2)*x 
            else:
                return self.myPow(1/x, -n)
