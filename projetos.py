import sys
import math

def somar_valores(numeros):
    return numeros * 2

atribuiçao = (somar_valores(10))

numeros  = [(sys.argv[1]),(sys.argv[2])]


atribuiçao_2 = math.fsum(numeros)

print(atribuiçao_2)