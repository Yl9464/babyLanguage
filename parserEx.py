class TreeNode:
    def __init__(self, srcToken):
        self.value = srcToken[0]
        self.token = srcToken[1]
        self.left = None
        self.right = None
        
def getPrecedence(op):
    if op in ["PLUS", "MINUS"]:
        return 1
    elif op in ["MULTIPLICATION", "DIVISION"]:
        return 2
    else:
        return 0

def parserEx(precedence, srcList):
    for i in range(len(srcList)):
        while len(srcList) > 1:
            nodes = TreeNode(srcList[i])
            print("nodes: ", nodes.value, nodes.token)
           
           #print("[1] ", srcList[1])
           #print("[2:] ",srcList[2:])
            break
     
            
    # while len(srcList) > 1:
    #     leftTree = TreeNode(srcList[0])
    #     print("leftTree: ", leftTree)
    #     op = TreeNode(srcList[1])
    #     print("op: ", op)
    #     curPrecedence = getPrecedence(op.token)
    #     print("curPrecedence: ", curPrecedence)
    # else:
        
  