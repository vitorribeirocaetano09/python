# desafio 01 :
ovo = True
massa = False
farinha = True
agua = True

fazer_bolo = massa or ovo and farinha or agua
nao_fazer_bolo = massa and ovo or farinha and agua

print("vamos fazer o bolo ? = {}, nao vamos fazer o bolo ! = {}".format(fazer_bolo,nao_fazer_bolo))