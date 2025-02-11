# Create a program to evaluate a house loan application. The monthly payment
# cannot exceed 30% of the applicant's salary, or the loan will be denied.

try:
    casaValor = int(input("Qual é o valor da casa? "))
    salarioValor = int(input("Quanto você ganha mensalmente? "))
    parcelamento = int(input("Em quantos anos você pretende pagar? "))
except ValueError:
    print("Por favor, insira apenas números inteiros.")
    exit()

limiteParcela = salarioValor * 0.30
quantidadeMeses = parcelamento * 12
parcelaMensal = casaValor / quantidadeMeses

if parcelaMensal > limiteParcela:
    print(f"Infelizmente sua solicitação de empréstimo foi negada, pois a parcela mensal de {parcelaMensal:.2f} reais excede 30% do seu salário ({limiteParcela:.2f} reais).")
else:
    print(f"O empréstimo foi aprovado. O valor mensal será de {parcelaMensal:.2f} reais.")
