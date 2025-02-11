# Function that calculates the area of a rectangular land.

def main():
    largura = getFloat("Digite a largura do terreno (m): ")
    comprimento = getFloat("Digite o comprimento do terreno (m): ")
    area(largura, comprimento)

def area(largura, comprimento):
    resultado = largura * comprimento
    print(f"A área do terreno de {largura:.2f}m x {comprimento:.2f}m é {resultado:.2f}m².")

def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

main()
