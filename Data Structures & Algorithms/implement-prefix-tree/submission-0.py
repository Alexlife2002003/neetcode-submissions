class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter]=TrieNode()
            cur=cur.children[letter]
        cur.end=True


    def search(self, word: str) -> bool:
        cur=self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur=cur.children[letter]
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur=cur.children[letter]
        return True
        
        