'''
@author Milagros Tamara Giraldo
@date May 2, 2026
Course: COMP 340-003
Description: Paerser file for the final project; final 
version compatible with minus sings and parenthesis.
'''
    

class TreeNode:
    def __init__(self, srcToken):
        self.value = srcToken[1] # [number,12] 
        self.token = srcToken[0]
        self.left = None
        self.right = None

weight = {
    "PLUS" : 1,
    "MINUS" : 1,
    "MULTIPLICATION" : 2,
    "DIVISION" : 2
}

def parserEX(srcList, precedence=0):
    
    first_item = srcList.pop(0)

    if first_item[0] == "MINUS":
        # if it is a negative number
        right = parserEX(srcList, 3)
        # it provides the list with the return of the values without the negative to then
        # add the negative sign to the value of the right node. with the logic of 0-1=-1
        zero = TreeNode(("NUMBER", 0))
        op_minus = TreeNode(("MINUS", "-"))
        op_minus.left = zero
        op_minus.right = right
        # op minus is the three with operation- and number 0 as the left node, and the number value as the right node.
        # making the value negative by doing 0 - n = -n
        # (0-n)
        left_tree = op_minus
        
    elif first_item[0] == "LPAREN":
        # cheking if we have a parenthesis. 
        left_tree = parserEX(srcList, 0) # the precedence value is still zero since we are currently just
        # looking at the parenthesis. not at any of the operators or at the order fo operation. 
        
        # on this if statement we call recursion on the list of tokens to get the value of the parenthesis. 
        # the recursion will end when we get to the right parenthesis.
        if srcList[0][0] != "RPAREN":
            raise SyntaxError("missing )") # complain when the right parenthesis is not found in the operation.

        srcList.pop(0) # removing the right parenthesis from the list of tokens.

    else:
        # otherwise the left three is just set to the first item of the list (this happens as 
        # default whwnever that items is not a negative number or a left parenthesis).
        left_tree = TreeNode(first_item)

    #  while loop for cheking that ll tokens of the source list are in the tree
    while len(srcList) > 0:
        # If the next token is not an operator, get out of the whole loop, 
        # meaning if the source list has only one value (which we alredy set to left tree, or if the value left on the list is not a +,-*,/ operator, 
        if srcList[0][0] not in weight:
            break

        op = srcList[0] # we get the operator
        curPrecedence = weight[op[0]] # set the current precednce based on the operator. 

        if curPrecedence <= precedence: # if the current operator has a greater weight then previus operator 
            # such as if is a multiplication with a weight if to, when the previus operator was 
            # a summation with a weight of 1, then we solve the current operator first and return it's resulting
            # node as if it was the value that will be given to the prvius operator.
            # otherwise we break out of the while loop. 
            break

        srcList.pop(0) # removing the operator from the list
        opNode = TreeNode(op) # making it a node

        right = parserEX(srcList, curPrecedence)

        opNode.left = left_tree
        opNode.right = right

        # we set the operator node with it's respective branches to be what we return
        left_tree = opNode

    return left_tree