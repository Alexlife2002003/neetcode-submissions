class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        seen=set(nums)
        for num in nums:
            cur=num
            longest=0
            while cur in seen:
                cur+=1
                longest+=1
            res=max(res, longest)
        return res