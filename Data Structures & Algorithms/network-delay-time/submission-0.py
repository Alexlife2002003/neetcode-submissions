class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minheap=[(0, k)]
        edges=defaultdict(list)
        result=0
        seen=set()
        for node, target, weight in times:
            edges[node].append((weight, target))

        
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in seen:
                continue
            
            seen.add(n1)
            result=w1
            

            for w2, n2 in edges[n1]:
                heapq.heappush(minheap, (w1+w2, n2))
        
        return result if len(seen) == n else -1

        
        