# excessoes de idades :

def comparaçao_idades(idade):
    
    
    if idade < 18:
        return "menor de idade"
    elif idade >= (18,25):
        return "idade ideal"
    elif idade>=(26,35):
        return "pode entrar a vontade"
    elif idade >= (36,45):
        return "velho demais para isso"
    else:
        return "idade nao digitada"
    
for a in (15,16,24,28,29,32,-11):
    print(f"{a} : {comparaçao_idades()}")