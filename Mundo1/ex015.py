# This program calculates the total cost of renting a car based on the number of days rented
# and kilometers driven. The daily cost is R$60.00, and the cost per kilometer is R$0.15.

dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
km = float(input("Digite a quantidade de quilômetros percorridos: "))

custoDias = dias * 60
custoKm = km * 0.15
custoTotal = custoDias + custoKm

print(f"O custo total é de R${custoTotal:.2f} (R${custoDias:.2f} pelos dias e R${custoKm:.2f} pelos quilômetros).")
