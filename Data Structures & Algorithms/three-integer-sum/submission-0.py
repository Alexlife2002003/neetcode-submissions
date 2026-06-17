class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for i, first in enumerate(nums):
            if first>0:
                continue
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left,right=i+1, len(nums)-1

            while left<right:
                three=first+nums[left]+nums[right]

                if three<0:
                    left+=1
                elif three>0:
                    right-=1
                else:
                    res.append([first, nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left-1]==nums[left]:
                        left+=1
        return res