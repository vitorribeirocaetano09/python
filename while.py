lista = ["compras","treinar","trabalhar"]

for i in lista:
    print(f"diario : {i}")
    
digitar_1 = input("qual a fazer concluiu :")

if digitar_1 in lista:
    print(f"elemento retirado : {digitar_1} retirado!")
    lista.remove(digitar_1)
    print(lista)

elif digitar_1 == "visitar":
    print(f"elemento nao recente : {digitar_1}")

else:
    print(f"elemento nao encontrado ou nao realizado : {digitar_1} ")