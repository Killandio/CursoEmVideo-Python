# Function that prints a message with a dynamic border.

def main():
    texto = getString("Digite uma mensagem: ")
    escreva(texto)

def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print("~" * tamanho)
    print(f"  {mensagem}  ")
    print("~" * tamanho)

def getString(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        else:
            print("Entrada inválida. Digite um texto não vazio.")

main()
