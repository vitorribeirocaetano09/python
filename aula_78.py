def calcular_notas():
    
    notas = float(input("digite a nota obtida :"))
    
    if notas == 10:
            print("nota execelente muito bem")
    elif notas >= 7.5:
        print("nota mediana,muito bem")
    elif notas >=4.6:
        print("nota baixa,melhore")
    
    else:
        print("nota absurdamente baixa,melhore")
        
if __name__=="__main__":
    
    resultado = calcular_notas()
    print(resultado)