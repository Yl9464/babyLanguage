import lexer
import re
# ops = {
#     "*": 2,
#     "/": 2,
#     "+": 1,
#     "-": 1,
#     "etc": 0
# }

# # root tree format #print(" ", i, "\n /", "\\\n")


def parseExpr(tokSeq):
    tokens = []
    for i in range(len(tokSeq)):
        # print(tokSeq[i])
        tokens.append(tokSeq[i])
    # print(len(tokens))
    if len(tokens) == 3:
        print(" ", tokSeq[1][-1], "\n /", "\\")  # operator
        if (tokSeq[0][-1] < tokSeq[2][-1]):  # left right operand
            print(tokSeq[0][-1], " ", tokSeq[2][-1])  # left right operand
        else:  
            print(tokSeq[2][-1], " ", tokSeq[0][-1])  # left right operand