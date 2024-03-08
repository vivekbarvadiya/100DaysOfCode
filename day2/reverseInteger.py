def fillzero(n):
    p=1
    while n:
        p*=10
        n=n-1
    return p

def len(n):
    count=0
    while n:
        n=int(n/10)
        count+=1
    return count

class Solution(object):
    def reverse(self, n):
        reverse=0
        num=n
        if n>2**31 or n<-2**31:
            return 0
        if n<0:
            n=-n
        while n>0:
            digit=n%10 # 3,2,1
            l=len(n//10) #2,1,0
            if l==0:
                reverse+=digit*(1)
            else:
                reverse+=digit*(10**l) # 300
            n=n//10 # 12
        if reverse>2**31 or reverse<-2**31:
            return 0
        if num<0:
            return -reverse
        return reverse