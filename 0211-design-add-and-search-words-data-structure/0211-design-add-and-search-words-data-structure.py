class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        """
            initialise a root TrieNode
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
            1. using a ptr to root,
            2. for every char in word,
            3. if it doesn't exist in the children, make TrieNode() for it
            4. move ptr to the next TrieNode
            5. set last character flag to True
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        """
            1. using a ptr to root,
            1b. make a dfs helper, with params j and root where j is the beginning of new word
            2. for every char in range j - word,
            3. if its not a dot, perform normal trie search
            4. if its a dot, perform dfs to search if the words after the dot match
            any child of the curr children values [dfs good here bc iterative requires too many checks]
            5. return False if a mismatch occurs (aka dfs returns False)
            6. return True if dfs is successful
            7. return curr.word outside of the function
            8. call dfs on 0 and root
        """
        curr = self.root

        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr =  curr.children[word[i]]
            return curr.word
        return dfs(0, curr)       

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)