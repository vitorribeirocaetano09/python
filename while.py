lista = None       
    
digitar = input("digite um nome :")

verificaçao = len(digitar)

if verificaçao >=6:
    print(f"obrigado usuario ----> : {digitar}")
    
elif verificaçao == 0:
    print("nome ou senha totalmente zerada :")
    
else:
    print("senha muito baixa!")