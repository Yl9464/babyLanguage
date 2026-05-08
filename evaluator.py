def evaluate(TreeRoot):
   
    if TreeRoot is None:
        return "ParseEx returned None"
    if TreeRoot.token == "NUMBER":
        value = int(TreeRoot.value)
    else:
        leftVal = evaluate(TreeRoot.left)
        rightVal = evaluate(TreeRoot.right)
        if TreeRoot.token == "PLUS":
            return leftVal + rightVal
        elif TreeRoot.token == "MINUS":
            return leftVal - rightVal
        elif TreeRoot.token == "MULTIPLICATION":
            return leftVal * rightVal
        elif TreeRoot.token == "DIVISION":
            return leftVal / rightVal
    return value
