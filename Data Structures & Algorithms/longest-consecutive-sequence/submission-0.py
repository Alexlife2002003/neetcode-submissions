class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        need=set(nums)

        for num in nums:
            streak=0
            cur=num
            while cur in need:
                streak+=1
                cur+=1
            res=max(res, streak)
        
        return res