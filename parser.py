import lexer
import re


# # root tree format #print(" ", i, "\n /", "\\\n")


def parseExpr(tokSeq):
    tokens = []
    for i in range(len(tokSeq)):
        tokens.append(tokSeq[i])

    if len(tokens) == 3:
        print(" ", tokSeq[1][-1], "\n /", "\\")  # operator
        if (tokSeq[0][-1] < tokSeq[2][-1]):  # left right operand
            print(tokSeq[0][-1], " ", tokSeq[2][-1])  # left right operand
        else:
            return (tokSeq[2][-1], " ", tokSeq[0][-1])
    elif len(tokens) == 5:
        for i in (range(len(tokens))):
            match tokens[i][-1]:
                case '+':
                    # print(tokens[i][-1])
                    print(" ", tokSeq[1][-1], "\n /", "\\")  # operator
                    if (tokSeq[0][-1] < tokSeq[2][-1]):  # left right operand
                        print(tokSeq[0][-1])
                case '-':
                    print(tokens[i][-1])
                    continue
                case '*':
                    print(tokens[i][-1])
                    #print(" ", tokSeq[1][-1], "\n /", "\\")  # operator
                   
                    continue
                case "/":
                    print(print(tokens[i][-1]))
                    continue
