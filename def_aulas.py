notas = [8,9,4,6,5,5,6]
media = 6

def calcular_notas():
    somar = sum(notas)
    subtrair = somar /media
    return subtrair

media_final = calcular_notas
print(f"notas disponiveis ------>")

if media_final == 20:
    print(f"a nota atingiu o esperado : {media_final}")

else:
    print(f"nota insulficiente")



    






