from tokens import RESERVED_WORDS, SPECIAL_SYMBOLS
import sys

class Tokenizer:
    def __init__ (self, filename):
        self._file = open(filename) #holds the file to parse
        self._tokens = [] #holds the array of tokens as tuples, eg: [(1,"program"), (31, "545")]
        self._cursor = 0 #holds the index of the token array we are currently looking at
        self._tokenizeLine()

    #Tokenizes a single line 
    def _tokenizeLine(self) -> None:
        self._tokens = []
        self._cursor = 0

        #Readslines until one has contnent or is at EOF
        line = self._file.readline()
        while line != "" and line.strip() == "":
            line = self._file.readline()
        if line == "":
            self._tokens.append((33, ""))
            self._file.close()
            return

        index = 0
        while(index < len(line)):
            #Reserved word branch
            if(line[index].islower()):
                index, tokenNum = self._readReserved(line, index)
                if(tokenNum == 34):
                    break
            #Integer branch
            elif(line[index].isdigit()):
                index, tokenNum = self._readInteger(line, index)
                if(tokenNum == 34):
                    break
            #Identifier Branch
            elif(line[index].isupper()):
                index, tokenNum = self._readIdentifier(line, index)
                if(tokenNum == 34):
                    break
            #Whitespace and newline branch
            elif(line[index].isspace()):
                index += 1
            #Special symbol Branch
            else:
                index, tokenNum = self._readSymbol(line,index)
                if(tokenNum == 34):
                    break

    #Gets the current token
    def getToken(self) -> int:
        return self._tokens[self._cursor][0]

    #Moves cursor to next token
    def skipToken(self) -> None:
        if(self._tokens[self._cursor][0] not in (33, 34)):
            self._cursor += 1
            if(self._cursor >= len(self._tokens)):
                self._tokenizeLine()

    #Returns token value if integer, else terminates
    def intVal(self) -> int:
        currToken = self._tokens[self._cursor]
        if currToken[0] == 31:
            return int(currToken[1])
        else:
            print("NOT AN INTEGER. TERMINATING PROGRAM...")
            sys.exit()

    #Returns token value if identifier, else terminates
    def idName(self) -> str:
        currToken = self._tokens[self._cursor]
        if currToken[0] == 32:
            return currToken[1]
        else:
            print("NOT AN IDENTIFIER. TERMINATING PROGRAM...")
            sys.exit()

    #Reads a reserved word token and adds it to the token array
    def _readReserved(self, line, index) -> tuple[int,int]:
        reservedWord = ""
        tokenNum = 34
        while(index < len(line) and line[index].islower() == True):
                reservedWord += line[index]
                index += 1

        if reservedWord in RESERVED_WORDS:
            tokenNum = RESERVED_WORDS.get(reservedWord)

        if index < len(line) and line[index].isalnum():
            tokenNum = 34

        self._tokens.append((tokenNum, reservedWord))
        return index, tokenNum


    #Reads a special symbol token and adds it to the token array
    def _readSymbol(self, line, index) -> tuple[int,int]:
        specialSymbol = line[index:index + 2]
        tokenNum = 34

        if specialSymbol not in SPECIAL_SYMBOLS:
            specialSymbol = line[index]

        if specialSymbol in SPECIAL_SYMBOLS:
            tokenNum = SPECIAL_SYMBOLS.get(specialSymbol)
        index += len(specialSymbol)

        self._tokens.append((tokenNum, specialSymbol))
        return index, tokenNum

    #Reads an integer token and adds it to the token array
    def _readInteger(self, line, index) -> tuple[int, int]:
        integer = ""
        tokenNum = 31

        while(index < len(line) and line[index].isdigit() == True):
                integer += line[index]
                index += 1

        if index < len(line) and line[index].isalnum():
            tokenNum = 34

        self._tokens.append((tokenNum, integer))
        return index, tokenNum


    #Reads an identifier token and adds it to the token array
    def _readIdentifier(self, line, index) -> tuple[int,int]:
        identifier = ""
        tokenNum = 32

        while(index < len(line) and (line[index].isupper() or line[index].isdigit())):
            identifier += line[index]
            index += 1
        
        if index < len(line) and line[index].isalnum():
            tokenNum = 34
        
        self._tokens.append((tokenNum, identifier))
        return index, tokenNum

        