# Ying Lu
# Comp340 - Parse HW
class TreeNode:
    def __init__(self, srcleftTree):
        self.value = srcleftTree[0]
        self.token = srcleftTree[1]
        self.left = None
        self.right = None


precDict = {
    "PLUS" : 1,
    "MINUS" : 1,
    "MULTIPLICATION" : 2,
    "DIVISION" : 2
}

def parseEx(srcList, precedence=0):
    item1 = srcList.pop(0)
    
    if item1[1] == "MINUS":
        right = parseEx(srcList, 3)
        
        zero = TreeNode((0, "NUMBER"))
        op_minus = TreeNode(("-", "MINUS"))
        
        op_minus.left = zero
        op_minus.right = right
        
        left_tree = op_minus
    elif item1[1] == "LPAREN":
         
        left_tree = parseEx(srcList, 0) 
        if srcList[0][0] != "RPAREN":
            raise SyntaxError("missing )") 
        srcList.pop(0)
    else:
        left_tree = TreeNode(item1)
    
    while len(srcList) > 0:
        if srcList[0][1] not in precDict:
            break
        op = srcList[0] 
        curPrecedence = precDict[op[1]]  

        if curPrecedence <= precedence: 
            break
        srcList.pop(0)
        opNode = TreeNode(op) # making it a node

        right = parseEx(srcList, curPrecedence)

        opNode.left = left_tree
        opNode.right = right
        left_tree = opNode
           
    return left_tree
    