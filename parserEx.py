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
    # Safety check
    if not srcList:
        return None, srcList

    # --- HANDLE FIRST ELEMENT (NUMBER / LPAREN / UNARY MINUS) ---

    token = srcList[0]

    # Case 1: Parentheses
    if token[1] == "LPAREN":
        leftTree, srcList = parserEx(0, srcList[1:])  # parse inside ()

        # consume RPAREN if present
        if srcList and srcList[0][1] == "RPAREN":
            srcList = srcList[1:]

    # Case 2: Unary minus
    elif token[1] == "MINUS":
        # parse right side with high precedence
        rightTree, srcList = parserEx(2, srcList[1:])

        zeroNode = TreeNode(["0", "NUMBER"])
        opNode = TreeNode(["-", "MINUS"])

        opNode.left = zeroNode
        opNode.right = rightTree

        leftTree = opNode

    # Case 3: Number
    else:
        leftTree = TreeNode(token)
        srcList = srcList[1:]

    # --- HANDLE BINARY OPERATIONS ---

    while srcList:
        # stop at closing parenthesis
        if srcList[0][1] == "RPAREN":
            break

        curToken = srcList[0]
        curPrecedence = getPrecedence(curToken[1])

        # stop if lower or equal precedence
        if curPrecedence <= precedence:
            break

        # consume operator
        opNode = TreeNode(curToken)

        # parse right side
        rightTree, srcList = parserEx(curPrecedence, srcList[1:])

        # build tree
        opNode.left = leftTree
        opNode.right = rightTree

        leftTree = opNode

    return leftTree, srcList
