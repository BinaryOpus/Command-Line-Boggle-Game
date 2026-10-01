from Trie.Trie import Trie
from Board.Tile import Tile
import random

class Board:
    
    def __init__(self, providedGrid = None):
        if providedGrid is None:
            self.grid = [[Tile(Board.__getSemiRandomCharacterFrequencyBased()) for _ in range(4)]for _ in range(4)]
        else:
            self.grid = providedGrid
        
        self.__generateBoardNeighbours()
        self.wordCount = 0
        self.boardTrie = Trie()
        self.__generateBoardTrie()
        
    
    def __str__(self):
        string = ""
        for row in self.grid:
            for tile in row:
                string += "[" + tile.character + "]"
            string += "\n"
        return string
    
    @staticmethod
    def __generateEnglishDictionaryTree():
        print("Generating English Dictionary...")
        tempEnglishDictionaryTrie = Trie()
        with open("Board/EnglishWords.txt", "r") as file:
            for line in file:
                word = line.strip()
                if len(word) >= 3:
                    tempEnglishDictionaryTrie.add(word)
        file.close()
        return tempEnglishDictionaryTrie
    
    englishDictionaryTrie = __generateEnglishDictionaryTree()
    
    @staticmethod
    def __getSemiRandomCharacterFrequencyBased():
    
        randomNumber = random.randint(0, 100)
        
        if randomNumber <= 5:
            return random.choice(Board.rareConsonantArray)
        elif 5 < randomNumber <= 35:
            return random.choice(Board.uncommonConsonantArray)
        elif 35 < randomNumber <= 75:
            return random.choice(Board.commonConsonantArray)
        else:
            return random.choice(Board.vowelArray)
    
    #No q because couldn't be bothered 
    vowelArray = ['a', 'e', 'i', 'o', 'u'] #25%
    commonConsonantArray = ['s', 'r', 'n', 't', 'l', 'c'] #40%
    uncommonConsonantArray = ['d', 'g', 'p', 'm', 'h', 'b', 'f'] #30%
    rareConsonantArray = ['y', 'v', 'k', 'w', 'z', 'x', 'j'] #5%
    
    '''
    Testing the code below
    '''
    
    def __generateBoardNeighbours(self):
        # I hate that this is hardcoded, but I just need a quick fix before I come up with a better implementation
        
        self.grid[0][0].neighbours = [self.grid[0][1],self.grid[1][1],self.grid[1][0]]
        self.grid[0][1].neighbours = [self.grid[0][0],self.grid[1][0],self.grid[1][1],self.grid[1][2],self.grid[0][2]]
        self.grid[0][2].neighbours = [self.grid[0][1],self.grid[1][1],self.grid[1][2],self.grid[1][3],self.grid[0][3]]
        self.grid[0][3].neighbours = [self.grid[0][2],self.grid[1][2],self.grid[1][3]]
        
        self.grid[1][0].neighbours = [self.grid[0][0],self.grid[0][1],self.grid[1][1],self.grid[2][1],self.grid[2][0]]
        self.grid[1][1].neighbours = [self.grid[0][1],self.grid[0][2],self.grid[1][2],self.grid[2][2],self.grid[2][1],self.grid[2][0],self.grid[1][0],self.grid[0][0]]
        self.grid[1][2].neighbours = [self.grid[0][2],self.grid[0][3],self.grid[1][3],self.grid[2][3],self.grid[2][2],self.grid[2][1],self.grid[1][1],self.grid[0][1]]
        self.grid[1][3].neighbours = [self.grid[0][3],self.grid[0][2],self.grid[1][2],self.grid[2][2],self.grid[2][3]]
        
        self.grid[2][0].neighbours = [self.grid[1][0],self.grid[1][1],self.grid[2][1],self.grid[3][1],self.grid[3][0]]
        self.grid[2][1].neighbours = [self.grid[1][1],self.grid[1][2],self.grid[2][2],self.grid[3][2],self.grid[3][1],self.grid[3][0],self.grid[2][0],self.grid[1][0]]
        self.grid[2][2].neighbours = [self.grid[1][2],self.grid[1][3],self.grid[2][3],self.grid[3][3],self.grid[3][2],self.grid[3][1],self.grid[2][1],self.grid[1][1]]
        self.grid[2][3].neighbours = [self.grid[1][3],self.grid[1][2],self.grid[2][2],self.grid[3][2],self.grid[3][3]]
        
        self.grid[3][0].neighbours = [self.grid[2][0],self.grid[2][1],self.grid[3][1]]
        self.grid[3][1].neighbours = [self.grid[3][0],self.grid[2][0],self.grid[2][1],self.grid[2][2],self.grid[3][2]]
        self.grid[3][2].neighbours = [self.grid[3][1],self.grid[2][1],self.grid[2][2],self.grid[2][3],self.grid[3][3]]
        self.grid[3][3].neighbours = [self.grid[2][3],self.grid[2][2],self.grid[3][2]]
    
    def __generateBoardTrie(self):
        #print("Generating Board Trie...")
        visitedTiles = []
        word = ""
       
        for row in self.grid:
            for tile in row:
                self.__generateBoardTrieHelper(tile, visitedTiles, word)
   
    def __generateBoardTrieHelper(self, tile, visitedTiles, word):
    
        visitedTiles.append(tile)
        word += tile.character
        
        if Board.englishDictionaryTrie.contains(word):
            self.boardTrie.add(word)
            self.wordCount += 1
        
        for neighbour in tile.neighbours:
        
            if (neighbour not in visitedTiles) and (Board.englishDictionaryTrie.containsPrefix(word)):
                self.__generateBoardTrieHelper(neighbour,visitedTiles,word)
      
        visitedTiles.remove(tile)
        word = word[:-1]