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


srcCode = "24+25"
tokSeq = lexer.tokenize(srcCode)
rootNode = parserEx.parserEx(0, tokSeq)
#printTree(rootNode)  # implementation of this function shown below
#print()
#Failed 
#  "23 * ((1+5) * 33)"
# "24"
# "125"
# "-5"
# "--5"
# "(-5)"


#Passed:
# "(1+2)*5+4"
#"1 * (2 + 5)"
#"1+2*5+15"