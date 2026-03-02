palavra = "vitor"
for letra in palavra:
    print(letra,end= "")
    
    
passed = ["rafaela","pedro","nicolas"]
for nomes in passed:
    print(f"{nomes}")

for posiçao,nomes in enumerate(passed):
    print(f"({posiçao})",nomes)
    
dias_semana = ["segunda","terça","quarta","quinta","sexta"]
for indice,posiçao in enumerate(dias_semana):
    print(f"{indice+1}",dias_semana)