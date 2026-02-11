from math import pi
import sys




def help():
    print("e necessario digitar um valor aqui ---> : ")



    
    
def calcula_circulo(raio):
    return pi*float(raio)*2

if len(sys.argv)<2:
    help()
    
elif not (sys.argv[1]).isnumeric:
    print("digite apenas um numero")
    sys.exit()
    
    
else:
    
    raio = (sys.argv[1])
    final = calcula_circulo(raio)
    print("valor do circulo e igual a ",final)