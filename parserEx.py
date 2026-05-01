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
    print(srcList)
    if not srcList:
        return None

    #leftTree
    token = srcList.pop(0)

    if token[1] == 'LPAREN':
        left = parserEx(0, srcList)

        if srcList and srcList[0][1] == 'RPAREN':
            srcList.pop(0)
        else:
            raise SyntaxError("Missing )")

    elif token[1] == 'NUMBER':
        left = TreeNode(token)

    else:
        raise SyntaxError(f"Unexpected token: {token}")

    # operators
    while srcList:
        next_token = srcList[0]

        if next_token[1] == 'RPAREN':
            break

 
        curPrecedence = getPrecedence(next_token[1])

        if curPrecedence <= precedence:
            break

        #Add perator
        op_token = srcList.pop(0)
        op_node = TreeNode(op_token)

        #RightTree
        right = parserEx(curPrecedence, srcList)

        op_node.left = left
        op_node.right = right

        left = op_node

    return left