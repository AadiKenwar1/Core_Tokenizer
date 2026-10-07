from tokenizer import Tokenizer


#Walks a whole file using the public interface and returns every token number
def allTokens(filename):
    t = Tokenizer(filename)
    tokens = []
    while True:
        token = t.getToken()
        tokens.append(token)
        if token in (33, 34):
            return tokens
        t.skipToken()

#Reads an _expected.txt file into a list of token numbers
def expectedTokens(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split()]


#Reserved Words Test
t = Tokenizer("test_files/reservedTest.txt")
assert t._tokens == [(1, "program"), (2, "begin"), (3, "end"), (4, "int")], t._tokens
print("Reserved Words Test Passed")

#Integer Test
t = Tokenizer("test_files/integerTest.txt")
assert t._tokens == [(31, "0"), (31, "5"), (31, "25"), (31, "1000"), (31, "42")], t._tokens
print("Integer Test Passed")

#Special Symbols Test
t = Tokenizer("test_files/symbolTest.txt")
assert t._tokens == [(12, ";"), (14, "="), (20, "("), (21, ")"), (29, "<=")], t._tokens
print("Special Symbols Test Passed")

#Identifier Test
t = Tokenizer("test_files/identifierTest.txt")
assert t._tokens == [(32, "AB12321"), (32, "FKSJ"), (32, "A12")], t._tokens
print("Identifier Test Passed")

#All 4 tokens test
t = Tokenizer("test_files/graderTest.txt")
assert t._tokens == [(1, "program"), (4, "int"), (32, "X"), (12, ";"), (2, "begin"),
            (32, "X"), (14, "="), (31, "25"), (12, ";"), (11, "write"),
            (32, "X"), (12, ";"), (3, "end")], t._tokens
print("Grader Test Passed")

#Sample 1 Test (full file, compared to the expected output)
result = allTokens("test_files/sample1.txt")
assert result == expectedTokens("test_files/sample1_expected.txt"), result
print("Sample 1 Test Passed")

#Sample 2 Test (full file, compared to the expected output)
result = allTokens("test_files/sample2.txt")
assert result == expectedTokens("test_files/sample2_expected.txt"), result
print("Sample 2 Test Passed")

#Sample 3 Test (full file, compared to the expected output)
result = allTokens("test_files/sample3.txt")
assert result == expectedTokens("test_files/sample3_expected.txt"), result
print("Sample 3 Test Passed")
