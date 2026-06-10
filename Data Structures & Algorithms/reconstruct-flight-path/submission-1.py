class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj= {src:[] for src, dst in tickets}
        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)
        
        result=["JFK"]

        def dfs(src):
            if len(tickets)+1 == len(result):
                return True

            if src not in adj:
                return False
            
            temp=list(adj[src])

            for i, dst in enumerate(temp):
                adj[src].pop(i)
                result.append(dst)
                if dfs(dst):
                    return True
                
                adj[src].insert(i, dst)
                result.pop()
            return False
        
        dfs("JFK")
        return result