from Trie.TrieRootNode import TrieRootNode
from Trie.TrieCharacterNode import TrieCharacterNode

class Trie:
    
    def __init__(self):
        self.root = TrieRootNode()

    def contains(self, word):
        if self.__contains(self.root, word) == True:
            #print("Does contain " + word)
            return True
        else:
            #print("Does not contain " + word)
            return False

    def __contains(self, childNode, word):
    
        if len(word) == 0:
            return False
        
        character = word[0]
        
        if character not in childNode.childDict:
            return False
            
        elif len(word) == 1 and childNode.childDict.get(character).completeWord:
            return True
            
        else:
            return self.__contains(childNode.childDict.get(character), word[1:])
    
    def containsPrefix(self, word):
        if self.__containsPrefix(self.root, word) == True:
            #print("Does contain prefix " + word)
            return True
        else:
            #print("Does not contain prefix " + word)
            return False

    def __containsPrefix(self, childNode, word):
    
        if len(word) == 0:
            return False
        
        character = word[0]
        
        if character not in childNode.childDict:
            return False
            
        elif len(word) == 1:
            return True
            
        else:
            return self.__containsPrefix(childNode.childDict.get(character), word[1:])
    
    
    def add(self, word):
        self.__add(self.root, word)

    def __add(self, childNode, word):
        
        character = word[0]
        
        if character not in childNode.childDict:
            childNode.childDict[character] = TrieCharacterNode(character)
   
        if len(word) == 1:
            childNode.childDict[character].completeWord = True
            #print(childNode.childDict[character].completeWord)
            return
       
        self.__add(childNode.childDict.get(character), word[1:])
    
    def print(self):
        word = ""
        self.__print(self.root, word)
   
    def __print(self, childNode, word):
        
        for key, value in childNode.childDict.items():
        
            #print(value , childNode.childDict[key].completeWord)
            word += value.character
            
            if childNode.childDict[key].completeWord == True:
                print(word)
    
            self.__print(value,word)
            word = word[:-1]
  
    def returnTrieAsList(self):
        word = ""
        wordList = []
        self.__returnTrieAsList(self.root, word, wordList)
        return wordList

    def __returnTrieAsList(self, childNode, word, wordList):
        for key, value in childNode.childDict.items():
        
            #print(value , childNode.childDict[key].completeWord)
            word += value.character
            
            if childNode.childDict[key].completeWord == True:
                wordList.append(word)
    
            self.__returnTrieAsList(value, word, wordList)
            word = word[:-1]