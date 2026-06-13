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
        
        result=set()
        visited=set()
        rows, cols = len(board), len(board[0])
        def dfs(r, c, cur, word):
            if r<0 or c<0 or r==rows or c==cols:
                return
            
            if (r,c) in visited or board[r][c] not in cur.children:
                return
            
            visited.add((r,c))
            word+=board[r][c]
            cur=cur.children[board[r][c]]
            if cur.end:
                result.add(word)
            dfs(r+1, c, cur, word)
            dfs(r, c+1, cur, word)
            dfs(r-1, c, cur, word)
            dfs(r, c-1, cur, word)
            visited.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)