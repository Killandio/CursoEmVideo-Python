# Shopping Analysis: Total Cost, Expensive Products, and Cheapest Item

def main():
    registrarProdutos()


def registrarProdutos():
    totalGasto = 0
    produtosMaisDeMil = 0
    produtoMaisBarato = ""
    menorPreco = float("inf")

    while True:
        nome = input("Digite o nome do produto: ").strip()
        preco = getPosFloat("Digite o preço do produto: R$ ")

        totalGasto += preco
        if preco > 1000:
            produtosMaisDeMil += 1
        if preco < menorPreco:
            menorPreco = preco
            produtoMaisBarato = nome

        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
        while continuar not in ("S", "N"):
            continuar = input("Opção inválida! Deseja continuar? [S/N]: ").strip().upper()

        if continuar == "N":
            break

    print("\nResultados:")
    print(f"Total gasto na compra: R$ {totalGasto:.2f}")
    print(f"Quantidade de produtos que custam mais de R$ 1000: {produtosMaisDeMil}")
    print(f"Produto mais barato: {produtoMaisBarato} custando R$ {menorPreco:.2f}")


def getPosFloat(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Erro: Apenas valores positivos são permitidos.")
            else:
                return value
        except ValueError:
            print("Erro: Digite um número válido.")


main()
