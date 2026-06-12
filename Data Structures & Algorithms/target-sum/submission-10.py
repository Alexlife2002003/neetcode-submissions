class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, suma):
            if i==len(nums):
                return 1 if target==suma else 0
            
            return dfs(i+1, suma+nums[i]) + dfs(i+1, suma-nums[i])
        
        return dfs(0,0)