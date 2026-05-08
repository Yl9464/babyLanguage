
class TreeNode:
    def __init__(self, treeData):
        self.value = treeData[0]
        self.token = treeData[1]
        self.left = None
        self.right = None


precDict = {
    "PLUS": 1,
    "MINUS": 1,
    "MULTIPLICATION": 2,
    "DIVISION": 2
}

def parseEx(srcList,precedence=0):
    print("parseEx srcList: ", srcList)
    print()
    # if len(srcList) == 0:
    #     return "Input Error"
    # item1 = srcList.pop(0)
    
    # if item1[1] == "MINUS":
    #     right = parseEx(srcList, 3)
    #     zero = TreeNode("0", "NUMBER")
    #     negative = TreeNode("-", "MINUS")
        
    #     zero = TreeNode("0", "NUMBER")
    #     negative.right = right
    #     leftTree = negative
        
    # elif item1[0] == "LPAREN":
    #     leftTree = parseEx(srcList, 0)
        
    #     if srcList[0][0] != "RPAREN":
    #         print("Missing closing parentheses")
    #     srcList.pop(0) #right paren 
    # else:
    #     leftTree = TreeNode(item1)
    
    # while len(srcList) > 0:
    #     if srcList[0][0] not in ("PLUS", "MINUS", "MULTIPLICATION", "DIVISION"):
    #         break
        
    #     op = srcList[0]
    #     curPrecedence = precDict[op[1]] #likely error
        
    #     if curPrecedence <= precedence:
    #         break
        
    #     srcList.pop(0)
    #     operation = TreeNode(op)
    #     right = parseEx(srcList, curPrecedence)
        
    #     operation.left = leftTree
    #     operation.right = right
        
    #     leftTree = operation
        
    # return leftTree
