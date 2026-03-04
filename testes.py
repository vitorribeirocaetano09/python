a = 30
b = 50

entrada = int(input("digite um numero ---->:"))

values = ((a+b)+(entrada))

try:
    saida = int(entrada)
    print("vc chegou no valor correto : ",values)

except ValueError :
    
    print("ops acho que digitou algo errado qui viu!")
    print("digite corretamente por favor")
    


