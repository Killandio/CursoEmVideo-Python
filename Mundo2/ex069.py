# User Input Validation and Data Analysis in a Modular Python Script

def main():
    cadastrarPessoas()

def cadastrarPessoas():
    mais18 = 0
    homens = 0
    mulheresMenos20 = 0

    while True:
        idade = getPosInt("Digite a idade: ")
        sexo = input("Digite o sexo [M/F]: ").strip().upper()

        while sexo not in ("M", "F"):
            sexo = input("Opção inválida! Digite o sexo [M/F]: ").strip().upper()

        if idade > 18:
            mais18 += 1
        if sexo == "M":
            homens += 1
        if sexo == "F" and idade < 20:
            mulheresMenos20 += 1

        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
        while continuar not in ("S", "N"):
            continuar = input("Opção inválida! Deseja continuar? [S/N]: ").strip().upper()

        if continuar == "N":
            break

    print("Resultados:")
    print(f"Quantidade de pessoas com mais de 18 anos: {mais18}")
    print(f"Quantidade de homens cadastrados: {homens}")
    print(f"Quantidade de mulheres com menos de 20 anos: {mulheresMenos20}")

def getPosInt(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Apenas números inteiros acima de zero são permitidos")
            else:
                return value
        except ValueError:
            print("Apenas números inteiros acima de zero são permitidos")
main()