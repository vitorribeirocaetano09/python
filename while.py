dados = ("vitor",1234)

while True:
    tentativa = input("digite seu nome :")
    tentativa_senha = int(input("digite a senha :"))
    
    if tentativa and tentativa_senha in dados:
        print("correto")
        break
    
    else:
        print("nao encontrado")
    
    
    
    
    


