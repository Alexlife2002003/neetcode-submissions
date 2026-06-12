class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
    
    def addWord(self, word):
        cur=self
        for letter in word:
            if letter not in cur.children:
                cur.children[letter]=TrieNode()
            cur=cur.children[letter]
        cur.end=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        res=set()
        visited=set()
        def dfs(r, c, node, word):
            if r<0 or c<0 or r==rows or c==cols:
                return
            
            if (r, c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r,c))
            word+=board[r][c]
            node=node.children[board[r][c]]
            if node.end:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)
        
        