
try:
    
    nota = input(float("digite um numero"))
        
    if nota == 10:
        for i in range(1,4):
             print(f"vc esta entre os top da escola agora : {i}")
    
    if nota >= 8.5:
        print(f"nota muito alta parabens")
        
    if nota >=6.5:
        print("nota mediana")
        
    if nota >=3.5:
        print("nota muito baixa")
        
    elif nota == 0:
        print("zerado")
         
         
except ValueError:
    print("valor inserido da nota errado tente novamente")

finally:
    print("obrigado por compartilhar notas")
            