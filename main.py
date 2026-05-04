# Ying Lu
# Comp340 - Evaluator HW
import lexer
import parseEx
import evaluator
import decipher

print("\nHello baby language.\nEnter baby exp and see what you get.")

while True:
    babyExp = input(">>> ")
    if babyExp == "poopoo":
        break
    srcCode = decipher.decipher(babyExp)
    print("Interpreted as: ", srcCode)
    srcList = lexer.tokenize(srcCode)
    rootNode, _ = parseEx.parseEx(0, srcList)
    result = evaluator.evaluate(rootNode)
    
    print("The result is: ", result)
print("Now it is time to go poo poo.")