import sys

class Brainfuck:
    """A brainfuck. """
    
    def __init__(self, code):
        """ (Brainfuck, str) -> NoneType

        A Brainfuck interpreter with code
        """
        self.code = "".join(filter(lambda x: x in '[>-+,.<]', code))
        self.cells = [0]
        self.ptr = 0

    def __str__(self):
        """ (Brainfuck) -> str

        Return a string representation of Brainfuck iterpreter

        >>> brnfck = Brainfuck('>>++')
        >>> brnfck.__str__()
        >>++
        """

        return self.code
    
    def increase(self):
        """ (Brainfuck) -> NoneType

        Increase value of the current cell.
        """
        if self.cells[self.ptr] < 255:
            self.cells[self.ptr] += 1
        else:
            self.cells[self.ptr] = 0

    def decrease(self):
        """ (Brainfuck) -> NoneType

        Decrease value of the current cell.
        """
        if self.cells[self.ptr] < 255:
            self.cells[self.ptr] -= 1
        else:
            self.cells[self.ptr] = 0

    def next(self):
        """ (Brainfuck) -> NoneType

        Increment the pointer.
        """
        self.prt += 1
        if self.prt == len(self.cells):
            self.cells.append(0)
            
    def back(self):
        """ (Brainfuck) -> NoneType

        Reduce the pointer.
        """
        if self.ptr == 0:
            self.ptr = len(self.cells) - 1
        else:
            self.ptr -= 1

    def outData(self):
        """ (Brainfuck) -> NoneType

        output the byte at the data pointer.
        """
        sys.stdout.write(chr(self.cells[self.ptr]))

    def inData(self):
        """ (Brainfuck) -> NoneType

        accept one byte of input, storing its value in the byte at the data pointer.
        """
        self.cells[self.ptr] = ord(sys.stdin.read(1))
        
    
