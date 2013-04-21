import sys

class Brainfuck:
    """A brainfuck. """
    
    def __init__(self, code):
        """ (Brainfuck, str) -> NoneType

        A Brainfuck interpreter with code
        """
        self._code = "".join(filter(lambda x: x in '[>-+,.<]', code))
        self._cells = [0]
        self._ptr = 0

    def __str__(self):
        """ (Brainfuck) -> str

        Return a string representation of Brainfuck iterpreter

        >>> brnfck = Brainfuck('>>++')
        >>> brnfck.__str__()
        >>++
        """
        return self._code

    def run(self):
        """ (Brainfuck) -> NoneType

        run app
        """
        self.perform(self._code)
        
    def perform(self, code):
        """ (Brainfuck, str) -> NoneType

        perform the code.
        """
        for x in code:
            if x == '+': self._increase()
            elif x == '-': self._decrease()
            elif x == '>': self_next()
            elif x == '<': self._back()
            elif x == '.': self._outData()
            elif x == ',': self._inData()
            
    
    def _increase(self):
        """ (Brainfuck) -> NoneType

        Increase value of the current cell.
        """
        if self._cells[self._ptr] < 255:
            self._cells[self._ptr] += 1
        else:
            self._cells[self._ptr] = 0

    def _decrease(self):
        """ (Brainfuck) -> NoneType

        Decrease value of the current cell.
        """
        if self._cells[self._ptr] < 255:
            self._cells[self._ptr] -= 1
        else:
            self._cells[self._ptr] = 0

    def _next(self):
        """ (Brainfuck) -> NoneType

        Increment the pointer.
        """
        self._ptr += 1
        if self._ptr == len(self._cells):
            self._cells.append(0)
            
    def _back(self):
        """ (Brainfuck) -> NoneType

        Reduce the pointer.
        """
        if self._ptr == 0:
            self._ptr = len(self._cells) - 1
        else:
            self._ptr -= 1

    def _outData(self):
        """ (Brainfuck) -> NoneType

        output the byte at the data pointer.
        """
        sys.stdout.write(chr(self._cells[self._ptr]))

    def _inData(self):
        """ (Brainfuck) -> NoneType

        accept one byte of input, storing its value in the byte at the data pointer.
        """
        self._cells[self._ptr] = ord(sys.stdin.read(1))

if __name__ == '__main__':

    bf = Brainfuck('++.')
    bf.run()
        
    
