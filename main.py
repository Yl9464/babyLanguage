# Ying Lu
# Comp340 - Parse HW
import lexer
import parseEx
import evaluator

while True:
    srcCode = input(">>>")
    if srcCode == "poopoo":
        break
   
    tokSeq = lexer.tokenize(srcCode)
    rootNode = parseEx.parseEx(tokSeq)
    result = evaluator.evaluate(rootNode)
    print("The result is: ", result)  # implementation of this function shown below
    print("Now it is time to go poo poo.")
