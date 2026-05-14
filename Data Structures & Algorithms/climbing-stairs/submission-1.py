class Solution:
    def climbStairs(self, n: int) -> int:
        first=1
        second=1

        for i in range(n-1): #because we already calculated one with the variables
            temp=first+second
            first=second
            second=temp
        
        return second
        