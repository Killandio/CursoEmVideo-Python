# Player vs Computer: Odd or Even Challenge

from random import randint

def jogarParImpar():
    vitorias = 0
    while True:
        jogador = int(input("Digite um número: "))
        escolha = input("Par ou Ímpar? [P/I]: ").strip().upper()
        computador = randint(0, 10)
        soma = jogador + computador
        resultado = "PAR" if soma % 2 == 0 else "ÍMPAR"

        print(f"Você jogou {jogador} e o computador {computador}. Total de {soma} deu {resultado}.")

        if (escolha == "P" and resultado == "PAR") or (escolha == "I" and resultado == "ÍMPAR"):
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break
        print("Vamos jogar novamente...\n")

    print(f"Fim do jogo! Você teve {vitorias} vitória(s) consecutiva(s).")


jogarParImpar()
