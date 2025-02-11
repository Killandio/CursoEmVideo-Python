# Program that manages the performance of a soccer player.
# It stores the number of matches and goals in a dictionary.

def main():
    aproveitamentoJogador = dict()
    aproveitamentoJogador["Nome"] = getString("Digite o nome do jogador: ")

    golsPorPartida = list()
    numPartidas = getInt(f"Quantas partidas {aproveitamentoJogador['Nome']} jogou? ")

    for i in range(numPartidas):
        golsPorPartida.append(getInt(f"Quantos gols ele fez na partida {i+1}: "))

    aproveitamentoJogador["Gols"] = golsPorPartida
    aproveitamentoJogador["Total"] = sum(golsPorPartida)  # Using sum() instead of manual sum

    print("-=" * 30)
    for chave, valor in aproveitamentoJogador.items():
        print(f"O campo {chave} tem valor {valor}")

    print("-=" * 30)
    print(f"O jogador {aproveitamentoJogador['Nome']} jogou {numPartidas} partidas")
    for i, gols in enumerate(golsPorPartida, start=1):
        print(f"Na partida {i}, ele marcou {gols} gols")

def getString(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        else:
            print("Entrada inválida. Insira uma string não vazia.")

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

main()
