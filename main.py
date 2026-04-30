import lexer
import parserEx

def printTree(treeRoot):
  if treeRoot.token == "NUMBER":
    print(treeRoot.value,end="")
  else:
    print("(",end="")
    printTree(treeRoot.left)
    print(treeRoot.value,end="")
    printTree(treeRoot.right)
    print(")",end="")
    
srcCode = "1 * (2 + 5)"
tokSeq = lexer.tokenize(srcCode)
rootNode = parserEx.parserEx(0, tokSeq)
printTree(rootNode) #implementation of this function shown below
print()


