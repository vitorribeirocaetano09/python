i = 0

while i <2:
    print(f"o comando começa com : {i}")
    i+=1
if i <= 2:
    print("codigo muito baixo")
else:
    print("codigo finalizado com sucesso")



print("ola usuario novo sera que pode assinar isso? :")

lista = ["vitor",1234]

while True:
    nome = input("digite para validar por favor  :")
    
    senha = int(input("digite a senha para validar :"))
    
    if nome and senha in lista :
        print(f"usuario encontrado com sucesso,pode continuar")
        break
        
    elif nome == lista:
        print("nome correto mais senha nao encontrada!")
    
    elif senha == lista:
        print("senha correta mais nome nao encontrado")
        
    else:
        print("usuario nao encontrado")