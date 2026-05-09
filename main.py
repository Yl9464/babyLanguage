# Comp340 - Evaluator HW
import lexer
import parseEx
import evaluator
import decipher

# print("\nHello baby language.\nEnter baby exp and see what you get.")

srcCode = decipher.decipher( "mama mama baaaaaba gah baaaa dada milk baaa dada")
print("Interpreted as: ", srcCode)
tokeSeq = lexer.tokenize(srcCode)
print("From lexer: ", tokeSeq)