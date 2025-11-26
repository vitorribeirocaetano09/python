saldo = 4500

valor = 3500

if saldo >=valor:
    print("saldo maior que o valor necessario : ",saldo)
else:
    print("saldo abaixo do valor necessario : ",saldo)



aluno_1 = 50
aluno_2= 45
alunos_3 = 60
aluno_4 = 75

media = 60

if aluno_1 >= media:
    print("aluno passou ",aluno_1)
elif aluno_2 >= media:
    print("aluno joao passou : ",aluno_2)
elif alunos_3 >= media:
    print("alunos maria passou : ",alunos_3)

else:
    print("nao passaram")
    
    
    

numero_secreto = None


for numeral in range(5,0,-1):
    print(f"contagem regressiva  : {numeral}")
    

print("encerrado comece!")


digitar = int(input("digite um valor para ganhar 10.000 : "))


if digitar >= 95:
    print("premio de elite realizado: tome : 10.000 ","valor digitado : ",digitar)

elif digitar >= 85:
    print("premio rasoavel realizado : tome : 6.000 ","valor digitado : ",digitar)

elif digitar >=70:
    print("premio baixo realizado : tome : 3.000 ","valor realizado :",digitar)


else:
    print("premio nao efetuado ou incorreto ! : ",digitar)