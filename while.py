lista = {"nome":"vitor","idade":16,"cidade":"carapicuiba"}

for nomes in lista.values():
    print(f"-----identidade : {nomes} ")
    variavel_chave = False
    
    while not variavel_chave:
        tentativa = input("poderia confirma se e realmente o senhor?(s/n) :")
        
    if tentativa == "s":
        print("tudo bem acesse o site :")
        break
    
    elif tentativa == "n":
        print("tudo bem pode ignorar a mensagem")
        break
    else:
        print("mensagem nao encontrada")
        
    
    print("fim da analise : ------> fim")