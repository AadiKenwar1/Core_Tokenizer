class Tokenizer:
    def __init__ (self, filename):
        self._file = openf(filename) #holds the file to parse
        self._tokens = [] #holds the array of tokens
        self._cursor = 0 #holds the index of the token array we are currently looking at
        

    

