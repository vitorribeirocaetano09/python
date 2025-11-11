# OPERADORES LOGICOS : AND,OR,NOT

# tabela verdade

# true and true = true
# true and false = false

# true or false = true
# true or true = true
# false or false = false

ensolarado = False
dia_chuvoso = True
dinheiro_na_conta = True

sair_de_casa = ensolarado or dia_chuvoso
ficar_em_casa = dinheiro_na_conta and ensolarado

print(sair_de_casa)
print(ficar_em_casa)

# exemplo 2 :

z = 3
b = 2
a = 1

comparaçao = (z>a or z<a)
print(comparaçao)

comparaçao_2 = (b>a and a<b)
print(comparaçao_2)

# tabela verdade xor,usado por != :

valor = True != False

valor_2 = False != False

# operador NOT :