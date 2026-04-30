class TreeNode:
    def __init__(self, srcToken):
        self.value = srcToken[0]
        self.token = srcToken[1]
        self.left = None
        self.right = None
        

    
def parserEx(precedence, srcList):
    
    if len(srcList) == 1:
        return TreeNode(srcList[0])
    else:
        leftTree = TreeNode(srcList[0])
        op = TreeNode(srcList[1])
        op.left = leftTree
        op.right = parserEx(precedence, srcList[2:])
        return op 

def printTree(treeRoot):
  if treeRoot.token == "NUMBER":
    print(treeRoot.value,end="")
  else:
    print("(",end="")
    printTree(treeRoot.left)
    print(treeRoot.value,end="")
    printTree(treeRoot.right)
    print(")",end="")
    