# COMP 340 HW5
# Ying Lu
import re
def tokenize(srcCode):
    
    srclist = []
    for i in range(len(srcCode)):
        value_type = None
        if re.search(r"[0-9]", srcCode[i]):
            if i > 0 and (re.search(r"[0-9]", srcCode[i-1])):
                print("srcCode[i]", srcCode[i])
                prev_value, prev_type = srclist[-1]
                srclist[-1] = (prev_value + srcCode[i], prev_type)
                continue
            else:
                value_type = "NUMBER"
        elif srcCode[i] == "+":
            value_type = "PLUS"
        elif srcCode[i] == "-":
            value_type = "MINUS"
        elif srcCode[i] == "*":
            value_type = "MULTIPLICATION"
        elif srcCode[i] == "/":
            value_type = "DIVISION"
        elif srcCode[i] == "(":
            value_type = "LPAREN"
        elif srcCode[i] == ")":
            value_type = "RPAREN"
        if value_type:
            srclist.append([srcCode[i], value_type])
    
    return srclist