class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges=defaultdict(list)

        for src, target, time in times:
            edges[src].append([time, target])
        
        heap=[(0,k)]
        visit=set()
        res=0

        while heap:
            time1, node1=heapq.heappop(heap)
            if node1 in visit:
                continue
            res=time1
            visit.add(node1)

            for time2, node2 in edges[node1]:
                if node2 not in visit:
                    heapq.heappush(heap, (time1+time2, node2))
        
        return res if len(visit)==n else -1