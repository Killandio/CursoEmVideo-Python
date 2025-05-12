def main():
    aproveitamento = dict()
    listaJogadores = list()
    gols = list()

    while True:
        aproveitamento.clear()
        gols.clear()
        aproveitamento["Nome"] = getName("Digite o nome do jogador: ")
        partidas = getInt(f"Quantas partidas {aproveitamento['Nome']} jogou? ")
        somaGols = 0

        for i in range(partidas):
            gols.append(getInt(f"Quantos gols ele fez na partida {i + 1}: "))
            somaGols += gols[i]

        aproveitamento["Gols"] = gols[:]
        aproveitamento["Total"] = somaGols
        listaJogadores.append(aproveitamento.copy())

        resposta = getString("Deseja cadastrar mais um jogador? [S/N]: ").upper()[0]
        while resposta not in "SN":
            print("Resposta inválida. Tente novamente!")
            resposta = getString("Deseja cadastrar mais um jogador? [S/N]: ").upper()[0]
            print()

        print("-=" * 30)
        if resposta == "N":
            while True:
                for i in range(len(listaJogadores)):
                    print(f"Código {i + 1} - {listaJogadores[i]['Nome']}")

                codigoJogador = getInt(f"Digite o código do jogador que deseja saber o aproveitamento ou {len(listaJogadores) + 1} para sair: ")
                while codigoJogador > len(listaJogadores) + 1:
                    print("Valor inválido. Tente novamente!")
                    codigoJogador = getInt(f"Digite o código do jogador que deseja saber o aproveitamento ou {len(listaJogadores) + 1} para sair: ")

                if codigoJogador == len(listaJogadores) + 1:
                    break

                print("-=" * 30)
                print(f"O jogador {listaJogadores[codigoJogador - 1]['Nome']}, jogou {len(listaJogadores[codigoJogador - 1]['Gols'])} partidas")
                print(f"Ele marcou um total de {listaJogadores[codigoJogador - 1]['Total']} gols")

                for i in range(len(listaJogadores[codigoJogador - 1]['Gols'])):
                    print(f"Na partida {i + 1}, marcou {listaJogadores[codigoJogador - 1]['Gols'][i]} gols")

                print("-=" * 30)
            break

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
        else:
            for character in userInput:
                if not (character.isalpha() or character.isspace()):
                    print("Entrada inválida. Por favor, digite um nome válido (apenas letras e espaços).")
                    break
            else:
                formattedInput = userInput.title()
                return formattedInput

def getInt(prompt):
    while True:
        try:
            userInput = input(prompt)
            return int(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")

main()
