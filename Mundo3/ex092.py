from datetime import datetime

# Program that reads name, birth year, work card, and calculates retirement age.

def main():
    anoAtual = datetime.now().year
    dadosPessoa = dict()

    dadosPessoa["Nome"] = getString("Nome: ")
    anoNascimento = getInt("Ano de nascimento: ")

    dadosPessoa["Idade"] = anoAtual - anoNascimento
    dadosPessoa["Ctps"] = getInt("Carteira de trabalho (0 não tem): ")

    if dadosPessoa["Ctps"] != 0:
        dadosPessoa["Contratação"] = getInt("Ano de contratação: ")
        dadosPessoa["Salário"] = getFloat("Salário: ")
        dadosPessoa["Aposentadoria"] = (dadosPessoa["Contratação"] + 35) - anoNascimento

    print("\nDados cadastrados:")
    for chave, valor in dadosPessoa.items():
        print(f"{chave}: {valor}")

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número decimal válido.")

def getString(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        else:
            print("Entrada inválida. Insira uma string não vazia.")

main()
