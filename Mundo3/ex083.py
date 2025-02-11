# Program that checks if a mathematical expression has correctly balanced parentheses.

def main():
    expressao = getString("Digite uma expressão matemática: ")
    pilha = list()

    for caractere in expressao:
        if caractere == "(":
            pilha.append("(")
        elif caractere == ")":
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(")")  # Unmatched closing parenthesis
                break

    if len(pilha) == 0:
        print("A expressão está válida! ✅")
    else:
        print("A expressão está inválida! ❌")

def getString(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        else:
            print("Entrada inválida. Insira uma string não vazia.")

main()
