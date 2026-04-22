import lexer
import re
ops = {
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1,
    "etc": 0
}

# root tree format #print(" ", i, "\n /", "\\\n")


def parseExpr(tokSeq):

    if len(tokSeq) == 3:
        print(" ", tokSeq[1][1], "\n /", "\\") # operator
        print(tokSeq[0][1], " ",tokSeq[2][1])  # left right operand

