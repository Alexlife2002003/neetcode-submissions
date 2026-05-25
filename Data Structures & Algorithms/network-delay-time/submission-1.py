class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        result=0
        visited=set()
        edges=defaultdict(list)

        for source, target, time in times:
            edges[source].append((time, target))
        
        minheap=[(0,k)]

        while minheap:
            time1, node1=heapq.heappop(minheap)
            if node1 in visited:
                continue
            visited.add(node1)
            result=time1

            for time2, node2 in edges[node1]:
                if node2 not in visited:
                    heapq.heappush(minheap, (time1+time2, node2))
        
        return result if len(visited)==n else -1