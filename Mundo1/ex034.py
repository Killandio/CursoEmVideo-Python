# This program calculates the salary increase for an employee:
# - If the salary is above R$1250, the increase is 10%.
# - Otherwise, the increase is 15%.

salario = float(input("Digite o salário do funcionário (em R$): "))

if salario > 1250:
    ajuste = salario + salario * 0.10
    print(f"Seu salário reajustado é {ajuste}")
elif 1250 >= salario > 0:
    ajuste = salario + salario * 0.15
    print(f"Seu salário reajustado é {ajuste}")
else:
    print("Salário inválido")