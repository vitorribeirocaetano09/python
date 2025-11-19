dicionario = {"nome":"vitor","cidade":"carapicuiba"}

for x,i in enumerate(dicionario):
    print("valor de x: ",x, "valor de i:", i)

dicionario_a = {"nome":"vitor","cidade":"carapicuiba","municipio":"osasco"}
print(len(dicionario_a))
print(dicionario_a["nome"])
print(dicionario_a["municipio"])
print(dicionario_a["cidade"])

for letras in dicionario_a.items():
    print(f"informaçoes do usuario : {letras}")
    

vitor = {"idade":16,"cidade":"carapicuiba"}

# forma de acessa valores mais facil :
print(vitor.keys())
print(vitor.values())
print(vitor.items())
print(vitor.pop("idade"))