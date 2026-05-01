import lexer
import parserEx


def printTree(treeRoot):
    if treeRoot.token == "NUMBER":
        print(treeRoot.value, end="")
    else:
        print("(", end="")
        printTree(treeRoot.left)
        print(treeRoot.value, end="")
        printTree(treeRoot.right)
        print(")", end="")


testCases = [
    "1*(2+5)",
     "(1+2)*5+4",
    "23 * ((1+5) * 33)",
    "24",
    "125",
    "-5",
    "--5",
    "(-5)",
    "1+2*5+15"
]

for case in testCases:
    srcCode = case
    tokSeq = lexer.tokenize(srcCode)
    rootNode, _ = parserEx.parserEx(0, tokSeq)
    printTree(rootNode)  # implementation of this function shown below
    print()

