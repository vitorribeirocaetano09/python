while True:
    dicionario = {"nome":"vitor","numero":42,"cidade":"carapicuiba","municipio":"osasco"}
    for i in dicionario.keys():
        print(f"o necessario por favor : {i}")
        
        mensagem = input("digite os valores correspondentes! :")
        if mensagem == "vitor":
            print(f"nome correto : {dicionario['nome']}")
            
        elif mensagem == 42:
            print(f"numero correto : {dicionario['numero']}")
            
        elif mensagem == "carapicuiba":
            print(f"cidade correto : {dicionario["cidade"]}")
            
        
        elif mensagem == "osasco":
            print(f"cidade correto : {dicionario["municipio"]}")
            
            
        
        else:
            print("icorreto ou inexistente")