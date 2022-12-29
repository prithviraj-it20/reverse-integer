class Solution:
    def reverse(self, x: int) -> int:
        a=0
        
        b=abs(x)
        while(b>0):
            remainder=b%10

            a=a*10+remainder
            b=int(b/10)
        if a>2147483647:
            return 0
        if x>=0:
            return a
        else:
            return -a
        
