# Read the employee's salary
salario = float(input("Digite o salário do funcionário (em R$): "))

# Calculate the new salary with a 15% raise
aumento = salario * 0.15
novo_salario = salario + aumento

print(f"O funcionário que ganhava R${salario:.2f}, com aumento de 15%, passará a receber R${novo_salario:.2f}.")
