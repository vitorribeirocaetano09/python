






tabuleiro = True
peças = False
regras_do_jogo = True
quantia_de_pessoas = False

jogar = tabuleiro and peças
desistir = peças or quantia_de_pessoas
observar = tabuleiro and regras_do_jogo

print("jogar = {} desistir = {} observar = {}".format(jogar , desistir, observar))