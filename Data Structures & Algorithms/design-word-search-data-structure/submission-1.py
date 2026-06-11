class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter]=TrieNode()
            cur=cur.children[letter]
        cur.end=True
        
    def search(self, word: str) -> bool:
        def dfs(j, child):
            for i in range(j,len(word)):
                letter=word[i]
                if letter==".":
                    for c in child.children.values():
                        if dfs(i+1, c):
                            return True
                    return False
                else:
                    if letter not in child.children:
                        return False
                    child=child.children[letter]
            return child.end
        
        return dfs(0, self.root)
        
