# Program that stores a list of products and their prices in a tuple.
# Then, it displays the data in a tabular format.

def main():
    produtos = (
        "Arroz", 5.50, "Feijão", 7.80, "Macarrão", 3.40, "Leite", 4.60,
        "Carne", 25.90, "Ovo", 12.30, "Pão", 6.00, "Queijo", 15.50
    )

    print("-" * 40)
    print(f"{'LISTAGEM DE PREÇOS':^40}")
    print("-" * 40)

    for i in range(0, len(produtos), 2):
        produto = produtos[i]
        preco = produtos[i + 1]
        print(f"{produto.ljust(30)}R$ {preco:>6.2f}")

    print("-" * 40)

main()
