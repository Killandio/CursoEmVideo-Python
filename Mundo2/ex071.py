# Simulating ATM Cash Withdrawal in Python

def main():
    valorSacado = getPosInt("Digite o valor a ser sacado (em reais): ")
    calcularNotas(valorSacado, 50)
    valorSacado %= 50
    calcularNotas(valorSacado, 20)
    valorSacado %= 20
    calcularNotas(valorSacado, 10)
    valorSacado %= 10
    calcularNotas(valorSacado, 1)

def calcularNotas(valor, nota):
    quantidadeNotas = valor // nota
    if quantidadeNotas > 0:
        print(f"Você receberá {quantidadeNotas} cédula(s) de R$ {nota}")

def getPosInt(prompt):
    while True:
        try:
            valor = int(input(prompt))
            if valor < 0:
                print("Erro: Apenas valores inteiros positivos são permitidos.")
            else:
                return valor
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

main()
