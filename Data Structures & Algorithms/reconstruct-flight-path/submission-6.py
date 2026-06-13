class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        edges=defaultdict(list)

        for src, dst in tickets:
            edges[src].append(dst)
        
        result = []

        def dfs(src):
            while edges[src]:
                next_dst=edges[src].pop()
                dfs(next_dst)
            result.append(src)
        
        dfs("JFK")
        return result[::-1]