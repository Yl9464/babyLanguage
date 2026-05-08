# COMP 340 HW5
# Ying Lu
import re
symbols = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "MULTIPLICATION",
    "/": "DIVISION",
    "(": "LPAREN",
    ")": "RPAREN"
}


def tokenize(srcCode):
    #print("lexer srcCode: ", srcCode)
    
    tokens = list(srcCode)
    srclist = []

    for i in range(len(tokens)):
        try:
            if tokens[i].isdigit():
                while i+1 < len(srcCode) and tokens[i+1].isdigit():
                    tokens[i] = tokens[i] + tokens.pop(i+1)
                srclist.append((tokens[i], "NUMBER"))
            else:
                token = symbols.get(tokens[i])
                if not token:
                    continue
                token = symbols.get(tokens[i])
        except IndexError:
            continue
    return srclist
