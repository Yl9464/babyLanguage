# Comp340 - Evaluator HW
import lexer
import parseEx
import evaluator
import decipher

# print("\nHello baby language.\nEnter baby exp and see what you get.")
# testcases = ["12*(2+5)", "(1+2)*5+4", "23*((1+5)*33", "24",
#              "125", "-5", "-5", "-(-5)", "poo poo"]

# decipher case: babapeebaaaaa
srcCode = decipher.decipher(
    "mama mama baaaaaba gah baaaa dada milk baaa dada")
print("Interpreted as: ", srcCode)
