from Trie.TrieNode import TrieNode

class TrieCharacterNode(TrieNode):
    
    def __init__(self, character):
        super().__init__()
        self.character = character
    
    def __str__(self):
        return "Value: " + self.character
 