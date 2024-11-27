# Read the product price
preco = float(input("Digite o preço do produto (em R$): "))

# Calculate the discounted price (5% off)
desconto = preco * 0.05
novo_preco = preco - desconto

print(f"O produto que custava R${preco:.2f}, com desconto de 5% custará R${novo_preco:.2f}.")
