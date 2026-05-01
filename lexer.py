# COMP 340 HW5
# Ying Lu
import re
import parserEx


def tokenize(srcCode):
    srclist = []
    i = 0
    while i < len(srcCode):
        if srcCode[i].isspace():
            i += 1
            continue

        if srcCode[i].isdigit():
            num = ""
            while i < len(srcCode) and srcCode[i].isdigit():
                num += srcCode[i]
                i += 1
            srclist.append([num, "NUMBER"])
            continue
        elif srcCode[i] == "+":
            srclist.append([srcCode[i], "PLUS"])
        elif srcCode[i] == "-":
            srclist.append([srcCode[i], "MINUS"])
            
        elif srcCode[i] == "*":
            srclist.append([srcCode[i], "MULTIPLICATION"])
        elif srcCode[i] == "/":
            srclist.append([srcCode[i], "DIVISION"])
        elif srcCode[i] == "(":
            srclist.append([srcCode[i], "LPAREN"])
        elif srcCode[i] == ")":
            srclist.append([srcCode[i], "RPAREN"])
        i+=1
    return srclist
   