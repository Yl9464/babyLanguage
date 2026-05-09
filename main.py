# Comp340 - Evaluator HW
import lexer
import parseEx
import evaluator
import decipher

def printTree(treeRoot):
    if treeRoot.token == "NUMB":
        print(treeRoot.value,end="")
    else:
        print("(",end="")
        printTree(treeRoot.left)
        print(treeRoot.value,end="")
        printTree(treeRoot.right)
        print(")",end="")
        
srcCode = decipher.decipher( "mama mama baaaaaba gah baaaa dada milk baaa dada")
print("Interpreted as: ", srcCode)
tokeSeq = lexer.tokenize(srcCode)

rootNode = parseEx.parseEx(tokeSeq)
print("From parser: ", printTree(rootNode))