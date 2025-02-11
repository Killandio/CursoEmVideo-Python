# Displays the terms of an arithmetic progression based on user input,
# allowing dynamic extension.

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Apenas números inteiros são permitidos.")

primeiroTermo = getInt("Digite o primeiro termo da PA: ")
razao = getInt("Digite a razão da PA: ")

termo = primeiroTermo
contador = 1
totalTermos = 10
mostrarMais = totalTermos

while mostrarMais != 0:
    while contador <= totalTermos:
        print(f"{termo}", end=" -> " if contador < totalTermos else " -> FIM\n")
        termo += razao
        contador += 1
    mostrarMais = getInt("Quantos termos mais você quer mostrar? (0 para sair): ")
    totalTermos += mostrarMais
