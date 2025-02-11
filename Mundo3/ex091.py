import random

# Program where 4 players roll a die and get random results.
# The results are stored in a dictionary and displayed in descending order.

def main():
    resultadoJogadores = {
        "Jogador 1": random.randint(1, 6),
        "Jogador 2": random.randint(1, 6),
        "Jogador 3": random.randint(1, 6),
        "Jogador 4": random.randint(1, 6)
    }

    print("\nResultados dos jogadores:")
    for jogador, resultado in resultadoJogadores.items():
        print(f"{jogador} tirou {resultado}")

    ranking = sorted(resultadoJogadores.items(), key=lambda x: x[1], reverse=True)

    print("\nRanking dos jogadores:")
    for posicao, (jogador, resultado) in enumerate(ranking, start=1):
        print(f"{posicao}° lugar: {jogador} com {resultado}")

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Número inválido. Digite um número válido.")

main()
