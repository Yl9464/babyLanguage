class TreeNode:
    def __init__(self, srcToken):
        self.value = srcToken[0]
        self.token = srcToken[1]
        self.left = None
        self.right = None


def ParserEx(srclist):
    if len(srclist) == 1:
        return TreeNode(srclist[0])

    leftTree = TreeNode(srclist[0])
    op = TreeNode(srclist[1])
    rightTree = ParserEx(srclist[2:])  # recursion

    op.left = leftTree
    op.right = rightTree
    return op
