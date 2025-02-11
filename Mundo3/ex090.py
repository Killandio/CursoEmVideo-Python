# Program that reads a student's name and average grade, storing their status in a dictionary.

def main():
    infoAluno = dict()

    infoAluno["Nome"] = getString("Digite o nome do aluno: ").title()
    infoAluno["Nota"] = getFloat(f"Digite a nota média do(a) {infoAluno['Nome']}: ")

    infoAluno["Situação"] = "Aprovado" if infoAluno["Nota"] >= 7 else "Reprovado"

    print("\nInformações do aluno:")
    for chave, valor in infoAluno.items():
        print(f"{chave}: {valor}")


def getString(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        else:
            print("Entrada inválida. Insira uma string não vazia.")


def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Número inválido. Digite um número válido.")


main()
