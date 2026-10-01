from Trie.Trie import Trie
from Board.Board import Board
from Board.Tile import Tile
from Board.Tile import Tile
import random
import math

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

gameActive = True

def __menuOptions():
    print("1 : Play Boggle \n2 : Exit Boggle")

def __menuSelection(userInput):

    try:
        userInput = int(userInput)
    except ValueError:
        print("Invalid input, try again")
        return
   
    match userInput:
        case 1:
            print("\033[H" + "\033[0J", end="")
            print("Starting Game...")
            boardActive = True
            board = Board()
            wordlist = []
            
            while boardActive:
                print("\nType the words you see in the grid, type '0' to stop the game")
                print(board)
                word = input()
                print("\033[H" + "\033[0J", end="")
                
                if word == "0":
                    print("\033[H" + "\033[0J", end="")
                    print(board)
                    trieAsList = board.boardTrie.returnTrieAsList()
                    print("You found" , len(wordlist),"/",len(trieAsList),"Words.")
                    print("Below is the grid of all possible words, the ones you found are green.\n")
                    
                    for word in trieAsList:
                        if word in wordlist:
                            print(color_text(word, 92), end =", ")
                        else:
                            print(word, end =", ")
                    print('\n')
                    boardActive = False
                    break
                else:
                    if board.boardTrie.contains(word) and word not in wordlist:
                        wordlist.append(word)
                        print(color_text("Congratulations, grid contains " + word + "!", 92)) # Green text
                        print(wordlist)
                    elif board.boardTrie.contains(word) and word in wordlist:
                        print(color_text("You have already found " + word + "!", 93)) # Yellow text
                        print(wordlist)
                    else:
                        print(color_text("Uh oh, grid doesn't contains " + word + "!", 91)) # Red text
                        print(wordlist)
       
        case 2:
            global gameActive
            gameActive = False
            print("Goodbye, thanks for playing")
        case _:
            print("Invalid number, try again")

print("Loading Game...")
print("Welcome to boggle, please select an option by typing the corresponding number")
while gameActive:
    __menuOptions()
    __menuSelection(input())
    
    
    
'''
def __menuSelection(userInput):

    try:
        userInput = int(userInput)
    except ValueError:
        print("Invalid input, try again")
        return
   
    match userInput:
        case 1:
            print("Starting Game...")
            boardActive = True
            board = Board()
            print(board)
            print("Type the words you see, type '0' to stop the game")
            
            wordlist = []
            
            while boardActive:
                word = input()
                if word == "0":
                    #print("\033[2K" + "\033[0B" + "\033[2K" + "\033[1B")
                    print("\033[2B")
                    boardActive = False
                    break
                else:
                    if board.boardTrie.contains(word) and word not in wordlist:
                        wordlist.append(word)
                        print("\033[2K" + color_text("Congratulations, grid contains " + word + "!", 92)) # Red text
                        print("\033[2K" + "Contains " + word , wordlist)
                        print("\033[3A" + "\033[2K" + "\033[1A")
                        
                    elif board.boardTrie.contains(word) and word in wordlist:
                        print("\033[2K" + color_text("You have already found " + word + "!", 93)) # Yellow text
                        print("\033[2A" + "\033[2K" + "\033[1A")
                        
                    else:
                        print("\033[2K" + color_text("Uh oh, grid doesn't contains " + word + "!", 91)) # Red text
                        print("\033[2K" + "Does not contain " + word , wordlist)
                        print("\033[3A" + "\033[2K" + "\033[1A")
        case 2:
            global gameActive
            gameActive = False
            print("Goodbye, thanks for playing")
        case _:
            print("Invalid number, try again")
            
'''