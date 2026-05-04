#import MilaParser

def evaluate(currNode):
    if currNode.token == "NUMBER":
        value = int(currNode.value)
    else:
        valueL = evaluate(currNode.left)
        valueR = evaluate(currNode.right)
        if currNode.token == "PLUS":
            value = valueL + valueR 
        elif currNode.token == "MINUS":
            value = valueL - valueR
        elif currNode.token == "MULTIPLICATION":
            value = valueL * valueR
        elif currNode.token == "DIVISION":
            value = valueL / valueR
    return value



# if __name__ == "__main__":
#     # testing evaluator by hand
#     root = MilaParser.TreeNode(["MINUS", "-"])
#     # root.left = paMilaParserrser.TreeNode(["NUMBER", "0"])
#     root.left = MilaParser.TreeNode(["DIVISION", "/"])
#     root.left.left = MilaParser.TreeNode(["NUMBER", "6"])
#     root.left.right = MilaParser.TreeNode(["NUMBER", "2"])
#     root.right = MilaParser.TreeNode(["PLUS", "+"])
#     root.right.left = MilaParser.TreeNode(["NUMBER", "3"])
#     root.right.right = MilaParser.TreeNode(["NUMBER", "4"])

#     print(evaluate(root)) # should print -4