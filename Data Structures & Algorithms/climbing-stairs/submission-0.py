class Solution:
    def climbStairs(self, n: int) -> int:
        first=1
        second=1

        for i in range(n-1):
            suma=first+second
            first=second
            second=suma
        
        return second
        