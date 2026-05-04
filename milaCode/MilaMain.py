import MilaLexer
import MilaParser
import MilaEvaluator

while True:
    srcCode = input(">>> ")
    if srcCode == "poopoo":
        break
    tokSeq = MilaLexer.lexer(srcCode)
    rootNode = MilaParser.parserEX(tokSeq)
    result = MilaEvaluator.evaluate(rootNode)
    print("The result is: ", result)
print("Now it is time to go poo poo.")