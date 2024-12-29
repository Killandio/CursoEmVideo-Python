# Calculates the final price of a product based on its payment method.
# Includes discounts and interest for different payment options.

def calcularPreco(preco, opcaoPagamento, parcelas = 1):
    if opcaoPagamento == 1:
        return preco * 0.90
    elif opcaoPagamento == 2:
        return preco * 0.95
    elif opcaoPagamento == 3:
        return preco
    elif opcaoPagamento == 4 and parcelas >= 3:
        return preco * 1.20
    else:
        return None

def getFloatInput(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Digite um número válido.")

def getIntInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Digite um número inteiro válido.")

precoProduto = getFloatInput("Digite o preço do produto: R$ ")
print("\nFormas de pagamento:")
print("1 - À vista (dinheiro/cheque): 10% de desconto")
print("2 - À vista no cartão: 5% de desconto")
print("3 - Em até 2x no cartão: preço normal")
print("4 - 3x ou mais no cartão: 20% de juros")

opcao = getIntInput("Escolha a opção de pagamento (1-4): ")

if opcao == 4:
    quantidadeParcelas = getIntInput("Quantas parcelas? ")
    if quantidadeParcelas < 3:
        print("Opção inválida: para 3x ou mais, escolha pelo menos 3 parcelas.")
    else:
        precoFinal = calcularPreco(precoProduto, opcao, quantidadeParcelas)
        print(f"\nPreço final: R$ {precoFinal:.2f} em {quantidadeParcelas}x (com juros).")
else:
    precoFinal = calcularPreco(precoProduto, opcao)
    if precoFinal is not None:
        print(f"\nPreço final: R$ {precoFinal:.2f}")
    else:
        print("Opção de pagamento inválida.")
