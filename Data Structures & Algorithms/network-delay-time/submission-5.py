class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges=defaultdict(list)
        for src, target, time in times:
            edges[src].append([time, target])
        minheap=[(0,k)]
        visit=set()
        result=0

        while minheap:
            time1, node1=heapq.heappop(minheap)
            if node1 in visit:
                continue
            
            result=time1
            visit.add(node1)

            for time2, node2 in edges[node1]:
                if node2 not in visit:
                    heapq.heappush(minheap, (time1+time2, node2))
        
        return result if len(visit)==n else -1