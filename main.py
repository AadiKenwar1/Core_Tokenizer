from tokenizer import Tokenizer
import sys

def main():
    #Checks that user has an input file
    if(len(sys.argv) != 2):
        print("INPUT FILE REQUIRED. TERMINATING PROGRAM...")
        sys.exit()

    #Creates tokenizer object
    inputFile = sys.argv[1]
    t = Tokenizer(inputFile)
    
    #iterates through all tokens until reaches EOF or illegal token
    while True:
        token = t.getToken()
        print(token)
        if(token == 33):
            print("Reached end of file!")
            break
        if(token == 34):
            print("ILLEGAL TOKEN FOUND")
            break
        t.skipToken()

if __name__ == "__main__":
    main()
