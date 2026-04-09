import re
# result = re.split(r'(\t)', "1+3")


def tokenize(srcCode):
    srclist = {}
    char = re.split(r'([+\-*/])', srcCode)

    for c in char:
       # print(c)
        if re.match(r'^[+-]?[0-9]+$', c):
            srclist[c] = "num"
       
        if c == '+':
            srclist[c] = "plus"
        elif c =='-':
            srclist[c] = "minus"
        elif c == '*':
            srclist[c] = "multiply"
        elif c =='/':
            srclist[c] = "divide"
    return srclist


print(tokenize("13+33"))
print(tokenize("1003-33"))
print(tokenize("666*566"))
print(tokenize("66/566"))
