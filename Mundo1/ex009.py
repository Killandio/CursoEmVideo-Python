# Read an integer and display its multiplication table from 1 to 10.

# Read an integer from the user
numero = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    tabuada = (numero * i)
    print(f"{i} x {numero} = {tabuada}")