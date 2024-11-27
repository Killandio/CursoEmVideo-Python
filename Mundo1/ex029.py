# This program checks if a driver is speeding and calculates the fine if they exceed 80 km/h.
# The fine is R$7.00 for each km above the speed limit.

velocidade = float(input("Digite a velocidade do carro (em km/h): "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você foi multado! O valor da multa é R${multa:.2f}.")
else:
    print("Velocidade dentro do limite. Tenha um bom dia!")
