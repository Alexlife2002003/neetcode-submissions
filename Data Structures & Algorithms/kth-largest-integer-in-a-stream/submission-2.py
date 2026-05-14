class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=nums
        heapq.heapify(self.heap)
        self.k=k
        while len(self.heap)>k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        cur=self.heap
        heapq.heappush(cur, val)
        if len(cur)>self.k:
            heapq.heappop(cur)
        
        return cur[0]
        
