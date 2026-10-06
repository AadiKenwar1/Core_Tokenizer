class Tokenizer:
    def __init__ (self, filename):
        self._file = open(filename) #holds the file to parse
        self._tokens = [] #holds the array of tokens
        self._cursor = 0 #holds the index of the token array we are currently looking at
        

    #program int X; begin X=25; write X; end
    def tokenizeLine(self):
        TODO

    def getToken() -> int:
        TODO

    def skipToken() -> None:
        TODO

    def intVal() -> int:
        TODO

    def idName() -> str:
        TODO

    def isInteger() -> bool:
        TODO

    def isIdentifier() -> bool:
        TODO