class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        tickets.sort(reverse=True)

        for src, dst in tickets:
            edges[src].append(dst)
        
        result=[]
        def dfs(src):
            while edges[src]:
                next_dst=edges[src].pop()
                dfs(next_dst)
            
            result.append(src)
        
        dfs("JFK")
        return result[::-1]
