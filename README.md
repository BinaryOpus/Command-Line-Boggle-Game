# Command-Line-Boggle-Game
Have you ever wanted to play the video game Boggle on the command-line interface? Well now you can! Test your knowledge of the English dictionary and see how many words you can find. This game is very simple to play, and strangely addictive.

## 🎮 Controls
Once the game has started, simply type the word you see and press enter to submit that word. Keep going until you cannot find any more words.
 
## 🛠️ Built With
This game is coded entirely in pure python, you won't need any external dependencies or third party libraries to enjoy this game.

## 🧮 How It Works
There are two main components to this code, the Trie(Prefix Tree) and the Board. The Trie is a prefix tree that stores all the words provided in the English dictionary text file. A trie is much more efficient for searching for searching for words as you don't have to continually iterate over each element in the list to search if it exists. Each node in the trie contains a dictionary where the key:value pair is character:node, the character acts as a key for another node further down the trie. The board is used to store the Boggle grid, each cell in the grid has a reference to its neighbours.

Below is an example of what the trie data structure looks like.
Trie contains these words (cat, car, can, dog)
the Trie looks like:

```text
(root)
├── c
│   └── a
│       ├── t ★
│       ├── r ★
│       └── n ★
└── d
    └── o
        └── g ★
```

## 🚀 Getting Started
Requirements:
 - Python

You can verify that Python is installed with:

    python --version

Clone the repository:

    git clone https://github.com/BinaryOpus/Command-Line-Boggle-Game.git

Navigate into the project:

    cd "Command-Line-Boggle-Game/src"
Run the game

    python main.py

## 🎯 Project Future Development
If I ever come to work on this project again there are several things I would like to develope further
 - At some point I would like to add a GUI to this game
 - I would like to add bigger grids to this game for example a 5x5 or 6x6 grid
 - Currently the generation of the characters in the Boggle board is random, this produces some boards with very few words in it. I would like to change this to create better boards with more words to find

## 📜 License
This project is licensed under the terms of the MIT License.
