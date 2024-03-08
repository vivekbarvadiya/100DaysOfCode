class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>1:
            sum=0
            n=str(n)
            for i in n:
                sum+=int(i)**2
            print(sum,n)
            n=sum
            if n==4:
                return False
        return True