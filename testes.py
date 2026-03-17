salario = 1000
taxa = 00,2

for mes in range(1,13):
    salario = salario+taxa
    print(f"mes {mes} acumulo : {round(salario,2)}")

