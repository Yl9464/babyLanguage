# Ying Lu
# Comp340 - Parse HW
class TreeNode:
    def __init__(self, srcleftTree):
        self.value = srcleftTree[1]
        self.token = srcleftTree[0]
        self.left = None
        self.right = None


precDict = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}

def printTree(treeRoot):
    if treeRoot.token == "NUMB":
        print(treeRoot.value,end="")
    else:
        print("(",end="")
        printTree(treeRoot.left)
        print(treeRoot.value,end="")
        printTree(treeRoot.right)
        print(")",end="")
        
def parseEx(srcList, precedence=0):
    print("start of parse: ", srcList)
    item1 = srcList.pop(0)
    # print("item1[0] ", item1[0])
    # if item1[0] == "-":
    #     right = parseEx(srcList,3)
    #     # print("right returned: ", right)
        
    #     zero = TreeNode(("0", "NUMBER"))
    #     op_minus = TreeNode(("-", "MINUS"))
    #     op_minus.left = zero
    #     op_minus.right = right
    #     left_tree = op_minus
    # if item1[0] == "(":
    #     #print("item1[0] = '(' ", srcList)
    #     #srcList
    #         # ['(', 'LPAREN'],
    #         # ['5', 'NUMBER1'], 
    #         # ['-', 'MINUS'], 
    #         # ['4', 'NUMBER'], 
    #         # [')', 'RPAREN'], 
    #         # ['*', 'MULTIPLICATION'], 
    #         # ['3', 'NUMBER'], 
    #         # [')', 'RPAREN']
    #     left_tree = parseEx(srcList,0)
    #     #print("left_tree returned: ", left_tree)
        
    #     #print("srcList[0][0] ~ ", srcList[0][0])
    #     #("srcList.pop(0) ", srcList.pop(0)) #['-', 'MINUS'] ['4', 'NUMBER']
    #     srcList.pop(0)
        
    # while len(srcList) > 0:
    #     #srcList[0][0] = -
    #     if srcList[0][0] not in precDict:
    #         break
    #     op = srcList[0] #['-','MINUS'] ['*', 'MULTIPLICATION']
        
    #     curPrec = precDict[op[0]] #1
    #     if curPrec <= precedence:
    #         break
    
    #     srcList.pop(0) #['-','MINUS'] ['*', 'MULTIPLICATION']
    #     opNode = TreeNode(op)
        
    #     right = parseEx(srcList, curPrec) #NONE
        
    #     opNode.left = left_tree #NONE
    #     opNode.right = right #NONE
    #     left_tree = opNode
    #     print("left_tree: ", left_tree)
    
    return 
