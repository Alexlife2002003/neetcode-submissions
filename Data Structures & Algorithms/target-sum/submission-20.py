class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(i, suma):
            if i==len(nums):
                return 1 if target==suma else 0
            
            if (i, suma) in memo:
                return memo[(i, suma)]
            addition=dfs(i+1, suma+nums[i])
            substraction=dfs(i+1, suma-nums[i])
            memo[(i, suma)]= addition+substraction
            return memo[(i, suma)]

        return dfs(0,0)