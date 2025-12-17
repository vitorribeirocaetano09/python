elo_estimado = 1500
elo_real = 2200
esperado = 1000

def calcular_rating():
    corte = (elo_estimado - esperado)/2
    comparaçao = (corte - elo_real)
    return comparaçao

realidade_rating = (esperado - calcular_rating())
print(f"rating esperado no final igual a : {realidade_rating}")

if realidade_rating >= 2556:
    print("meus parabens vc e um grao mestre : ------>")

else:
    print("vc e um candidato a mestre ainda :  ----->")