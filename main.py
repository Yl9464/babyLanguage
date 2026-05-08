# Ying Lu
# Comp340 - Decipher HW
import lexer
import parseEx
import evaluator
import decipher

#print("\nHello baby language.\nEnter baby exp and see what you get.")


#babyExp = "baaaaamilkmamababaagahbaaaaadada" 
babyExp= "baaaaa gahba baaa heh baa bapeebaa ba milk baaaaaa"
#Interpreted as: 5-13/21+21*6
#The result is: 130.38095238095238
input = " ".join(babyExp.split())
# if babyExp == "poopoo":
#     break

srcCode = decipher.decipher(input)

print("Interpreted as: ", srcCode) #11+5

print("srcCode passed to lexer: ",srcCode)
srcList = lexer.tokenize(srcCode)

print("srcList passed to parser: " , srcList)
rootNode = parseEx.parseEx(srcList)

print("rootNode passed to Evaluator: ", rootNode)
result = evaluator.evaluate(rootNode)

#print("The result is: ", result) #16
#print("Now it is time to go poo poo.")

