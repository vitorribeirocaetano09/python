capital = int(input("digite seu capital aqui --> :"))
taxa_mensal = float(input("digite uma taxa --> :"))
periodo = int(input("periodo estimado : "))

if __name__ == "__main__":
    calculo_simples = (capital*taxa_mensal*periodo)
    montante = capital + calculo_simples
    
    for contas in (calculo_simples,montante):
        print(f"situaçao atual -----> : ",contas)
    
    if contas >= int(1250):
        soma_nova = montante + 100
        print("seu novo montante em cima do valor do banco e igual a :",soma_nova)
    
    else:
        soma_subtraida = montante-float(2.55)
        print("montante alterado,verifique com a agencia bancaria : ",soma_subtraida)
        
        
        