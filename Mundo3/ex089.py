# Program that reads the name and two grades of multiple students and stores them in a list.
# At the end, it displays a report with the average grade of each student
# and allows the user to view individual grades.

def main():
    listaAlunos = []

    while True:
        nome = getString("Digite o nome do aluno: ")
        nota1 = getFloat("Digite a primeira nota: ")
        nota2 = getFloat("Digite a segunda nota: ")

        media = (nota1 + nota2) / 2
        aluno = [nome, [nota1, nota2], media]
        listaAlunos.append(aluno)

        continuar = getString("Deseja continuar? [S/N]: ").upper()
        while continuar[0] not in "SN":
            print("Opção inválida! Digite 'S' para continuar ou 'N' para sair.")
            continuar = getString("Deseja continuar? [S/N]: ").upper()

        if continuar[0] == "N":
            break

    print("\nBoletim dos alunos:")
    for aluno in listaAlunos:
        print(f"Nome: {aluno[0]}, Média: {aluno[2]:.2f}")

    mostrarNotas(listaAlunos)

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
            userInput = input(prompt)
            return float(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")

def mostrarNotas(listaAlunos):
    while True:
        nome = getString("\nDigite o nome do aluno para ver as notas ou 'Sair' para encerrar: ")
        if nome.lower() == "sair":
            break

        for aluno in listaAlunos:
            if aluno[0].lower() == nome.lower():
                print(f"Notas de {aluno[0]}: {aluno[1]}")
                break
        else:
            print("Aluno não encontrado. Tente novamente.")

main()
