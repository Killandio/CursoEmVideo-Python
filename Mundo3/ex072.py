# Program that reads a number (0 to 20) and displays it in full text.
# Uses a tuple for storing the numbers in words.

def main():
    numerosExtenso = (
        "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
        "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
        "dezoito", "dezenove", "vinte"
    )

    numero = getNumberInRange("Digite um número entre 0 e 20: ")
    print(f"Você digitou o número {numerosExtenso[numero]}.")

def getNumberInRange(prompt):
    while True:
        try:
            numero = int(input(prompt))
            if 0 <= numero <= 20:
                return numero
            else:
                print("Por favor, escolha um número entre 0 e 20.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

main()
