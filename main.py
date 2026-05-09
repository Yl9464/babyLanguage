# Comp340 - Evaluator HW
import lexer
import parseEx
import evaluator
import decipher


srcCode = decipher.decipher("mama mama baaaaaba gah baaaa dada milk baaa dada")

print("Interpreted as: ", srcCode)

tokeSeq = lexer.tokenize(srcCode)
print("tokeSeq parser: ", tokeSeq)
rootNode = parseEx.parseEx(tokeSeq)
# print("From parser: ", rootNode)
