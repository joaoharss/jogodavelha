import functions as tad_jogo_da_velha


def main():
    tabela = ["_"] * 9
    jogador = 1
    jogador_num_1 = 0
    jogador_num_2 = 0

    nome_jogador_1 = input("Digite o nome do jogador 1: ")
    simb1 = input(f"Digite o simbolo do {nome_jogador_1}: ")
    nome_jogador_2 = input("Digite o nome do jogador 2: ")
    simb2 = input(f"Digite o simbolo do {nome_jogador_2}: ")

    breakpoint = True
    while breakpoint:
        print()
        print(tad_jogo_da_velha.cria_tabela(tabela))
        if jogador == 1:
            jogador_num_1 = int(input(
                f"Digite a posição que o {nome_jogador_1} deseja jogar (de 1 a 9): "))
            if tad_jogo_da_velha.verifica_posicao(tabela, (jogador_num_1 - 1)):
                tabela[jogador_num_1 - 1] = simb1
                print(tad_jogo_da_velha.cria_tabela(tabela))
                if tad_jogo_da_velha.verifica_vitoria(tabela, simb1):
                    print(f"O jogador {nome_jogador_1} venceu.")
                    breakpoint = False
                if tad_jogo_da_velha.verifica_empate(tabela):
                    print("Empatou")
                    breakpoint = False
                if breakpoint:
                    jogador = 2
            else:
                print(tad_jogo_da_velha.cria_tabela(tabela))
                print("Posição ocupada")

        # vez do jogador num2
        if jogador == 2:
            jogador_num_2 = int(input(
                f"Digite a posição que o {nome_jogador_2} deseja jogar (de 1 a 9): "))
            if tad_jogo_da_velha.verifica_posicao(tabela, (jogador_num_2 - 1)):
                tabela[jogador_num_2 - 1] = simb2
                print(tad_jogo_da_velha.cria_tabela(tabela))
                if tad_jogo_da_velha.verifica_vitoria(tabela, simb2):
                    print(f"O jogador {nome_jogador_2} venceu! ")
                    breakpoint = False
                if tad_jogo_da_velha.verifica_empate(tabela) and breakpoint:
                    print("Empatou!")
                    breakpoint = False
                if breakpoint:
                    jogador = 1
            else:
                print(tad_jogo_da_velha.cria_tabela(tabela))
                print("Posição ocupada")


main()
