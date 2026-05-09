# Comp340 - Evaluator HW
import lexer
import parseEx
import evaluator
import decipher

#tests:
#   gahbaaaba
#   mama mama baaaaaba gah baaaa dada milk baaa dada
#   baaaaa gah ba baaa heh baa bapeebaa ba milk baaaaaa
#   mama mama baaaaaba gah baaaa dada milk baaa dada
srcCode = decipher.decipher("baaaaa gah ba baaa heh baa bapeebaa ba milk baaaaaa")

print("Interpreted as: ", srcCode)

tokeSeq = lexer.tokenize(srcCode)
rootNode = parseEx.parseEx(tokeSeq)
result = evaluator.evaluate(rootNode)
print("The result is: ", result)



