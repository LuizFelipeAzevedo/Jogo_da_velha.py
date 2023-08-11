import velha as v

tab = v.criaTabuleiro()
#v.imprime(tab)
player = 'X'

while v.temEspaco(tab) and not v.haGanhador(tab):
    v.imprime(tab)
    print("Jogador " + player)
    l = int(input("linha: "))
    c = int(input("coluna: "))
    resp = v.joga(tab, l, c, player)
    if resp:
        player = v.trocaJogador(player)
    else:
        print("Jogada inválida!")

if v.haGanhador(tab):
    player = v.trocaJogador(player)
    print("Parabens, jogador", player, 'venceu')
else:
    print("Deu velha!")            

v.imprime(tab)    