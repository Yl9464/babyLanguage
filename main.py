import lexer
import parserEx
import evaluator

srcCode = "2 + 3 * 4"
tokSeq = lexer.tokenize(srcCode)
rootNode = parserEx.parserEx(0, tokSeq)
result = evaluator.evaluate(rootNode)

parserEx.printTree(rootNode) #implementation of this function shown below
print()

print("Resuult: ", result)

