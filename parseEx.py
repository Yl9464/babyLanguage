class TreeNode:
    def __init__(self, srcleftTree):
        self.value = srcleftTree[0]
        self.token = srcleftTree[1]
        self.left = None
        self.right = None

precDict = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}

def parseEx(srcList, precedence=0):
    item1 = srcList.pop(0)
    
    if item1[0] == "-":
        right = parseEx(srcList,3)
        
        zero = TreeNode(("0", "NUMBER"))
        op_minus = TreeNode(("-", "MINUS"))
        op_minus.left = zero
        op_minus.right = right
        left_tree = op_minus
    
    elif item1[0] == "(":
        left_tree = parseEx(srcList, 0)
        srcList.pop(0)  
    
    else:
        left_tree = TreeNode(item1) 
         
    while len(srcList) > 0:
        if srcList[0][0] not in precDict:
            break
        op = srcList[0]
       
        curPrec = precDict[op[0]] #1
        if curPrec <= precedence:
            break
    
        srcList.pop(0)
        opNode = TreeNode(op)
        
        right = parseEx(srcList, curPrec) 
       
        opNode.left = left_tree 
        opNode.right = right 
        left_tree = opNode

    return left_tree

