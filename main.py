# Ying Lu
# Comp340 - Parse HW
import lexer
import parseEx
import evaluator


def printTree(treeRoot):
    if treeRoot.token == "NUMBER":
        print(treeRoot.value, end="")
    else:
        print("(", end="")
        printTree(treeRoot.left)
        print(treeRoot.value, end="")
        printTree(treeRoot.right)
        print(")", end="")


while True:
    srcCode = input(">>> ")
    if srcCode == "poopoo":
        break
    tokSeq = lexer.tokenize(srcCode)
    rootNode, _ = parseEx.parseEx(0, tokSeq)
    result = evaluator.evaluate(rootNode)
    print("The result is: ", result)
print("Now it is time to go poo poo.")
