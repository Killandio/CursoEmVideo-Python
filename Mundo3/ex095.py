# Program that manages the performance of multiple soccer players.
# It stores data for multiple players, including their match statistics.

def main():
    listaJogadores = list()

    while True:
        aproveitamentoJogador = dict()
        golsPorPartida = list()

        aproveitamentoJogador["Nome"] = getName("Digite o nome do jogador: ")
        numPartidas = getInt(f"Quantas partidas {aproveitamentoJogador['Nome']} jogou? ")

        for i in range(numPartidas):
            golsPorPartida.append(getInt(f"Quantos gols ele fez na partida {i + 1}: "))

        aproveitamentoJogador["Gols"] = golsPorPartida
        aproveitamentoJogador["Total"] = sum(golsPorPartida)  # Using sum() for efficiency
        listaJogadores.append(aproveitamentoJogador.copy())

        resposta = getString("Deseja cadastrar mais um jogador? [S/N]: ").upper()
        while resposta not in "SN":
            print("Resposta inválida. Tente novamente!")
            resposta = getString("Deseja cadastrar mais um jogador? [S/N]: ").upper()

        print("-=" * 30)
        if resposta == "N":
            break

    mostrarDetalhes(listaJogadores)

def mostrarDetalhes(listaJogadores):
    while True:
        print("\nLista de jogadores cadastrados:")
        for i, jogador in enumerate(listaJogadores, start=1):
            print(f"Código {i} - {jogador['Nome']}")

        codigoJogador = getInt(f"Digite o código do jogador para ver detalhes ou {len(listaJogadores) + 1} para sair: ")
        while codigoJogador < 1 or codigoJogador > len(listaJogadores) + 1:
            print("Valor inválido. Tente novamente!")
            codigoJogador = getInt(f"Digite o código do jogador para ver detalhes ou {len(listaJogadores) + 1} para sair: ")

        if codigoJogador == len(listaJogadores) + 1:
            break

        jogadorSelecionado = listaJogadores[codigoJogador - 1]
        print("-=" * 30)
        print(f"Nome: {jogadorSelecionado['Nome']}")
        print(f"Total de partidas: {len(jogadorSelecionado['Gols'])}")
        print(f"Total de gols: {jogadorSelecionado['Total']}")

        for i, gols in enumerate(jogadorSelecionado["Gols"], start=1):
            print(f"Na partida {i}, marcou {gols} gols")

        print("-=" * 30)

def getString(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        else:
            print("Entrada inválida. Por favor, digite uma string não vazia.")

def getName(prompt):
    while True:
        userInput = input(prompt).strip()
        if not userInput:
            print("Entrada inválida. O nome não pode estar vazio.")
        elif not all(c.isalpha() or c.isspace() for c in userInput):
            print("Entrada inválida. Por favor, digite um nome válido (apenas letras e espaços).")
        else:
            return userInput.title()

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

main()
