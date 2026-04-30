class TreeNode:
    def __init__(self, srcToken):
        self.value = srcToken[0]
        self.token = srcToken[1]
        self.left = None
        self.right = None
        
# precedenceDict = {
#     '+': 1,
#     '-': 1,
#     '*': 2,
#     '/': 2
# }
def getPrecedence(srcToken):
    if srcToken in ("PLUS", "MINUS"):
        return 1
    elif srcToken in ("MULTIPLICATION", "DIVISION"):
        return 2
    else:
        return 0
    
def parserEx(precedence, srcList):
    
    if len(srcList) == 1:
        leftTree = TreeNode(srcList[0])
        op = TreeNode(srcList[1])
        curPrecedence = getPrecedence(srcList[1][1])
       #print("currentPrecedence: ", curPrecedence)
        
        if precedence < curPrecedence:
            op.left = leftTree
            op.right = parserEx(precedence, srcList[2:])
            return op
        else:        
            return leftTree
    else:
        return TreeNode(srcList[0])
    
