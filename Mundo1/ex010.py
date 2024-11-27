# Read an amount of money in BRL from the user.
# Calculate how much USD the user can buy based on a fixed exchange rate.
# Display the converted amount.

# Read the amount of money the user has in BRL
reais = float(input("Digite quanto dinheiro você tem na carteira (em R$): "))

# Define a fixed exchange rate (BRL to USD)
taxaCambio = 5.81  # Dollar value on November 26, 2024

dolares = reais / taxaCambio

print(f"Com R${reais:.2f}, você pode comprar US${dolares:.2f}.")
