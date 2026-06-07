class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result=max(piles)
        right=result
        left=1

        while left<=right:
            k=(left+right)//2

            hours=0
            for pile in piles:
                hours+=math.ceil(pile/k)
            
            if hours<=h:
                result=k
                right=k-1
            else:
                left=k+1
        return result