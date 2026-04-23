from parserEx import ParserEx
from lexer import tokenize
from printTree import printTree

srcCode = "1 + 3 * 4"
srcList = tokenize(srcCode)
rootNode = ParserEx(srcList)

printTree(rootNode) 
print()