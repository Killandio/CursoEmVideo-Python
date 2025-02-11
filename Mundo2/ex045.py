# Simulates a Rock-Paper-Scissors game between the user and the computer.
# The computer makes a random choice, and the game decides the winner.

import random

def escolhaComputador():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    return random.choice(opcoes)

def escolhaUsuario():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")
        try:
            escolha = int(input("Digite o número da sua escolha: "))
            if escolha in [1, 2, 3]:
                return ["Pedra", "Papel", "Tesoura"][escolha - 1]
            else:
                print("Escolha inválida. Selecione 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def determinarVencedor(escolhaUsuario, escolhaComputador):
    if escolhaUsuario == escolhaComputador:
        return "Empate!"
    elif (escolhaUsuario == "Pedra" and escolhaComputador == "Tesoura") or \
         (escolhaUsuario == "Papel" and escolhaComputador == "Pedra") or \
         (escolhaUsuario == "Tesoura" and escolhaComputador == "Papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"

escolhaComputador = escolhaComputador()
escolhaUsuario = escolhaUsuario()

print(f"\nVocê escolheu: {escolhaUsuario}")
print(f"O computador escolheu: {escolhaComputador}")
print(determinarVencedor(escolhaUsuario, escolhaComputador))
