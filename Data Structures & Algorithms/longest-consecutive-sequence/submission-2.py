class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        res=0

        for num in nums:
            streak=0
            cur=num
            while cur in seen:
                cur+=1
                streak+=1
            
            res=max(res, streak)
        
        return res