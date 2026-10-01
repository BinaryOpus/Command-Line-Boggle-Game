class Tile:
    def __init__(self, character):
        self.character = character
        self.neighbours = []
    
    def __str__(self):
        return "[" + self.character +"]"