class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def backtrack(i, suma):
            if i==len(nums):
                return 1 if suma==target else 0

            if (i, suma) in memo:
                return memo[(i, suma)]
            
            add=backtrack(i+1, suma+nums[i])
            substract= backtrack(i+1, suma-nums[i])

            memo[(i, suma)] = add+substract

            return memo[(i, suma)]
        
        return backtrack(0,0)