'''
@author Milagros Tamara Giraldo
@date April 18, 2026
Course: COMP 340-003
Description: Lexer for the final project
'''
import re

def lexer(string):
    list_of_values = [] # [[category, 1],[category, 2],...] [category, 12]
    
    for i in range(len(string)):
        value_type = ""
        
        # case statmment does not naturally works well with regex so
        # instead of using a case statemnt used a chain of ifelse statemets.
        if bool(re.search(r"[0-9]", string[i])):
            if i > 0 and bool(re.search(r"[0-9]", string[i-1])):
                list_of_values[-1][1] += string[i]
                value_type = "" # no new value is appended to the "list_of_values".
            else: # when the value is a single number or is the first number. 
                value_type = "NUMBER"
        elif string[i] == "+":
            value_type = "PLUS"
        elif string[i] == "-":
            value_type = "MINUS"
        elif string[i] == "*":
            value_type = "MULTIPLICATION"
        elif string[i] == "/":
            value_type = "DIVISION"
        elif string[i] == "(":
            value_type = "LPAREN"
        elif string[i] == ")":
            value_type = "RPAREN"
            
        if value_type =="": # when the string is a space number or non valid value.
            continue
        else:
            list_of_values.append([value_type, string[i]])
    return list_of_values

# the function has no error cheking.
# a second way of doing the lexer.
# symbols = {
#     "+" : "plus",
#     "-" : "minus",
#     "*" : "mult",
#     "/" : "div",
#     "(" : "Lpar",
#     ")" : "Rpar"
# }

# def tokenizer(x):
#     tokens = list(x)
#     tokenmpa = []
#     # print(tokens)
#     for i in range(len(tokens)):
#         try:
#             if tokens[i].isdigit(): 
#                 while i+1 < len(tokens) and tokens[i+1].isdigit():
#                     tokens[i] = tokens[i]+ tokens.pop(i+1)
#                 tokenmpa.append((tokens[i],"num"))
#             else:
#                 token = symbols.get(tokens[i])
#                 if not token:
#                     continue
#                 tokenmpa.append((tokens[i],token))
#         except IndexError:
#             continue
#     return tokenmpa
            
# tok = tokenizer("1+(2+3)+374732")
# print(tok)