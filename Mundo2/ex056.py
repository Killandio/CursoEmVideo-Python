# Calculates the average age, finds the oldest man, and counts women under
# 20 years old

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Digite apenas números, por favor.")

somaIdades = 0
maiorIdadeHomem = 0
nomeMaisVelho = ""
totalMulheresMenos20 = 0

for p in range(1, 5):
    print(f"---- {p}ª PESSOA ----")
    nome = input("Nome: ").strip()
    idade = getInt("Idade: ")
    sexo = input("Sexo [M/F]: ").strip().upper()
    somaIdades += idade

    if sexo == "M" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome

    if sexo == "F" and idade < 20:
        totalMulheresMenos20 += 1

mediaIdade = somaIdades / 4

print(f"\nA média de idade do grupo é de {mediaIdade:.1f} anos.")
if maiorIdadeHomem > 0:
    print(f"O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeMaisVelho}.")
else:
    print("Não há homens no grupo.")
print(f"Ao todo são {totalMulheresMenos20} mulheres com menos de 20 anos.")
