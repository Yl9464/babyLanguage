class TreeNode:
    def __init__(self, srcleftTree):
        self.value = srcleftTree[0]
        self.token = srcleftTree[1]
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
    if not srcList:
        return None, srcList

    leftTree = srcList[0]

    if leftTree[1] == "LPAREN":
        leftTree, srcList = parserEx(0, srcList[1:])

        if srcList and srcList[0][1] == "RPAREN":
            srcList = srcList[1:]

    elif leftTree[1] == "MINUS":
        rightTree, srcList = parserEx(2, srcList[1:])

        minusZero = TreeNode(["0", "NUMBER"])
        op = TreeNode(["-", "MINUS"])

        op.left = minusZero
        op.right = rightTree

        leftTree = op

    else:
        leftTree = TreeNode(leftTree)
        srcList = srcList[1:]

    while srcList:
        if srcList[0][1] == "RPAREN":
            break

        curToken = srcList[0]
        curPrecedence = getPrecedence(curToken[1])

        if curPrecedence <= precedence:
            break

        op = TreeNode(curToken)

        rightTree, srcList = parserEx(curPrecedence, srcList[1:])

        # build tree
        op.left = leftTree
        op.right = rightTree

        leftTree = op

    return leftTree, srcList
