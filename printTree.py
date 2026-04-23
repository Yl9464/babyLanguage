def printTree(treeRoot):
    if treeRoot.token == "NUMBER":
        print(treeRoot.value, end="")
    else:
        print("(", end="")
        printTree(treeRoot.left)
        print(treeRoot.value, end="")
        printTree(treeRoot.right)
        print(")", end="")  
