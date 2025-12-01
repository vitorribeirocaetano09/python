# saldo = 4500

# valor = 3500

# if saldo >=valor:
#     print("saldo maior que o valor necessario : ",saldo)
# else:
#     print("saldo abaixo do valor necessario : ",saldo)



# aluno_1 = 50
# aluno_2= 45
# alunos_3 = 60
# aluno_4 = 75

# media = 60

# if aluno_1 >= media:
#     print("aluno passou ",aluno_1)
# elif aluno_2 >= media:
#     print("aluno joao passou : ",aluno_2)
# elif alunos_3 >= media:
#     print("alunos maria passou : ",alunos_3)

# else:
#     print("nao passaram")
    
    
    

# numero_secreto = None


# for numeral in range(5,0,-1):
#     print(f"contagem regressiva  : {numeral}")
    

# print("encerrado comece!")


# digitar = int(input("digite um valor para ganhar 10.000 : "))


# if digitar >= 95:
#     print("premio de elite realizado: tome : 10.000 ","valor digitado : ",digitar)

# elif digitar >= 85:
#     print("premio rasoavel realizado : tome : 6.000 ","valor digitado : ",digitar)

# elif digitar >=70:
#     print("premio baixo realizado : tome : 3.000 ","valor realizado :",digitar)


# else:
#     print("premio nao efetuado ou incorreto ! : ",digitar)
    

# pessoa = "vitor"

# idade = 25

# cpf = True

# if pessoa == "vitor" and idade >=16 and cpf == True:
#     print("pessoa encontrada com sucesso!")
# else:
#     print("pessoa nao encontrada!")





# saldo_inicial = 15000

# dividas_externas = True

# rendimento_futuro = True

# print(f"iremos avaliar suas condiçoes bancarias,com o valor : {saldo_inicial:2f}")

# if saldo_inicial >= 10000 and dividas_externas == True and rendimento_futuro == True:
#     print("conta bancaria de acordo com o esperado")

# else:
#     print("conta bancaria desigual!")
   


# inicial = 2

# while inicial<=10:
#     print("valores : ",inicial)
#     inicial+=1




# comando = None

# while comando != "sair":
    
#     digitar = input("digite um comando para sair : ")
#     if digitar == "entra":
#         print("entrando dentro de arquivos :",digitar)
#     elif digitar == "reset":
#         print("comando sendo totalmente resetado:",digitar)
#     else:
#         print("comando nao encontrado !:",digitar)
        
        
        
        

a = 55
b = 102

if a!=b:
    print("e diferente")
else:
    print("e igual")
    
    
    
c = "vitor"
d = "joao"

if c == d:
    print("igual")
elif d!=c:
    print("diferente")
    
    

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






