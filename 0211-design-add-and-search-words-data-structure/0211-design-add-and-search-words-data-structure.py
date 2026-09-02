class TrieNode:
    def __init__(self):
        self.children = {}
        self.exit = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.exit = True
        

    def search(self, word: str) -> bool:
        def dfs(root,ind):
            cur = root
            for i in range(ind,len(word)):
                ch = word[i]
                if ch == ".":
                    for child in cur.children.values():
                        if dfs(child,i+1):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return cur.exit
        return dfs(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)