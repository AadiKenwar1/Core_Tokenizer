Core Tokenizer
Author: Aadi Kenwar

FILES
main.py                 - Main file. Takes an input file name from the command line and prints each token number.
tokenizer.py            - The Tokenizer class (constructor, getToken, skipToken, intVal, idName) and its private helper methods.
tokens.py               - Dictionaries for the reserved words (1-11) and special symbols (12-30).
test.py                 - Unit tests that check the Tokenizer against small input files.
README.txt              - This file.
documentation.txt       - Design description, user manual, testing summary, and known bugs.
 
TEST FILES
test_files/reservedTest.txt    - Input with only reserved words 
test_files/integerTest.txt     - Input with only integers 
test_files/symbolTest.txt      - Input with only special symbols 
test_files/identifierTest.txt  - Input with only identifiers 
test_files/graderTest.txt      - Short Core program mixing all four token kinds 
test_files/sample1.txt         - Sample Core program 1
test_files/sample1_expected.txt - Expected token output for sample1.txt
test_files/sample2.txt         - Sample Core program 2
test_files/sample2_expected.txt - Expected token output for sample2.txt
test_files/sample3.txt         - Sample Core program 3
test_files/sample3_expected.txt - Expected token output for sample3.txt

HOW TO RUN
    python main.py <input_file>

Example:
    python main.py test_files/sample1.txt

The program prints one token number per line. It stops after printing 33 (end of file)
or 34 (illegal token), and prints a short message saying which one it hit.

HOW TO RUN THE TESTS
    python test.py

Each test prints a whether it passed. A failed test stops the test suite with an AssertionError.

NOTES
- Written in Python. Requires Python 3.9 or newer.
