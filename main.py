# Comp340 - Evaluator HW
import lexer
import parseEx
import evaluator
import decipher

#tests:
# babapeebaaaaa
# baaaaab
# gahbaaaba
# baaaaa milk mamababaa gah baaaaa dada
# baaaaa gah ba baaa heh baa bapeebaa ba milk baaaaaa
# mama mama baaaaaba gah baaaa dada milk baaa dada

print("\nHello baby language.\nEnter baby exp and see what you get.")
while True:
    babyExp = input(">>> ")
    if babyExp == "poopoo":
        break
    srcCode = decipher.decipher(babyExp)
    print("Interpreted as: ", srcCode)
    srcList = lexer.tokenize(srcCode)
    rootNode = parseEx.parseEx(srcList)
    result = evaluator.evaluate(rootNode)
    print("The result is: ", result)
print("Now it is time to go poo poo.")

# srcCode = decipher.decipher("baaaaa gah ba baaa heh baa bapeebaa ba milk baaaaaa")
# print("Interpreted as: ", srcCode)
# tokeSeq = lexer.tokenize(srcCode)
# rootNode = parseEx.parseEx(tokeSeq)
# result = evaluator.evaluate(rootNode)
# print("The result is: ", result)



