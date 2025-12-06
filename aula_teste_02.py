lista = [22,33]
while True:
    
    numero_digitar = int(input("digite um numero : "))
    if numero_digitar >= 10:
        somando = sum(lista)
        print(f"valor : {numero_digitar},esta de acordo com caso :")
        print(f"soma ocorrida com sucesso ------> : {somando}")
        break
    
    elif numero_digitar == 0:
        print("saindo do programa")
        
    else:
        print(f"numero nao encontrado : {numero_digitar}")
        print("tente novamente em ------")