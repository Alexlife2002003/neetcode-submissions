class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = [-x for x in stones]
        heapq.heapify(minheap)

        while len(minheap)>1:
            stone1=heapq.heappop(minheap)
            stone2=heapq.heappop(minheap)

                
            if stone2>stone1:
                heapq.heappush(minheap, (stone1-stone2))
                
        
        return -minheap[0] if minheap else 0

        