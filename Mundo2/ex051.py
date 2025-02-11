# Reads the first term and the common difference of an AP, then
# calculates and displays its first 10 terms.

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Digite apenas números inteiros, por favor!")

primeiroTermo = getInt("Digite o primeiro termo da PA: ")
razao = getInt("Digite a razão da PA: ")

for i in range(10):
    termo = primeiroTermo + i * razao
    print(f"O {i+1}º termo é: {termo}")
