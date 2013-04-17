class Brainfuck:
    def __init__(self):
        self.cells = [bytes(0)]
        self.ptr = 0
    def increase(self):
        self.cells[self.ptr] += 1
    
