# Program that registers multiple people, storing name, gender, and age in a dictionary.
# It calculates the number of women, the average age, and lists people above the average age.

def main():
    pessoasCadastradas = list()
    idadeAcimaMedia = list()
    cadastrarPessoa = dict()

    somaIdades = 0
    quantidadeMulheres = 0

    while True:
        cadastrarPessoa.clear()
        cadastrarPessoa["Nome"] = getName("Digite o nome da pessoa: ")
        cadastrarPessoa["Idade"] = getInt(f"Digite a idade de {cadastrarPessoa['Nome']}: ")

        cadastrarPessoa["Sexo"] = getString(f"Digite o sexo de {cadastrarPessoa['Nome']} [M/F]: ").upper()
        while cadastrarPessoa["Sexo"] not in "MF":
            print("Erro! Digite apenas M (masculino) ou F (feminino).")
            cadastrarPessoa["Sexo"] = getString("Digite o sexo [M/F]: ").upper()

        pessoasCadastradas.append(cadastrarPessoa.copy())
        somaIdades += cadastrarPessoa["Idade"]

        if cadastrarPessoa["Sexo"] == "F":
            quantidadeMulheres += 1

        resposta = getString("Deseja cadastrar mais alguém? [S/N]: ").upper()
        while resposta not in "SN":
            print("Erro! Digite apenas S (Sim) ou N (Não).")
            resposta = getString("Deseja cadastrar mais alguém? [S/N]: ").upper()

        if resposta == "N":
            break

    mediaIdades = somaIdades / len(pessoasCadastradas)

    for pessoa in pessoasCadastradas:
        if pessoa["Idade"] > mediaIdades:
            idadeAcimaMedia.append(pessoa["Nome"])

    print("\n" + "-=" * 30)
    print(f"A quantidade de pessoas cadastradas foi: {len(pessoasCadastradas)}")
    print(f"A quantidade de mulheres é: {quantidadeMulheres}")
    print(f"A média de idade do grupo é: {mediaIdades:.2f}")

    if idadeAcimaMedia:
        print(f"As pessoas com idade acima da média são: {idadeAcimaMedia}")
    else:
        print("Não há pessoas com idade acima da média!")

def getName(prompt):
    while True:
        userInput = input(prompt).strip()
        if not userInput:
            print("Entrada inválida. O nome não pode estar vazio.")
        elif not all(c.isalpha() or c.isspace() for c in userInput):
            print("Entrada inválida. Digite um nome válido (letras e espaços apenas).")
        else:
            return userInput.title()

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

def getString(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        else:
            print("Entrada inválida. Por favor, digite uma string não vazia.")

main()
