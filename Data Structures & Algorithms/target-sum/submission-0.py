class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways=0

        def dfs(i, suma):
            nonlocal ways
            if i==len(nums) and suma==target:
                ways+=1
                return 
            if i==len(nums):
                return
            
            dfs(i+1, suma+nums[i])
            dfs(i+1, suma-nums[i])
        


        dfs(0,0)
        return ways