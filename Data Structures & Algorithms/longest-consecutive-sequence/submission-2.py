class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        seen=set(nums)

        for num in nums:
            longest=0
            cur=num
            while cur in seen:
                longest+=1
                cur+=1
            res=max(res, longest)
        
        return res