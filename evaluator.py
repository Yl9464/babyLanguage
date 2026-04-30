def evaluate(TreeRoot):
    if TreeRoot.token == "NUMBER":
        return int(TreeRoot.value)
    leftVal = evaluate(TreeRoot.left)
    rightVal = evaluate(TreeRoot.right)
    
    if TreeRoot.value == "PLUS":
        return leftVal + rightVal
    elif TreeRoot.value == "MINUS":   
        return leftVal - rightVal
    elif TreeRoot.value == "TIMES":
        return leftVal * rightVal
    elif TreeRoot.value == "DIVIDE":
        return leftVal / rightVal
    