# This program reads a full name from the user and analyzes it by displaying:
# 1. The name in uppercase.
# 2. The name in lowercase.
# 3. The total number of letters (excluding spaces).
# 4. The number of letters in the first name.

nomeCompleto = input("Digite seu nome completo: ")

nomeMaiusculo = nomeCompleto.upper()
nomeMinusculo = nomeCompleto.lower()
totalLetras = len(nomeCompleto.replace(" ", ""))
letrasPrimeiroNome = len(nomeCompleto.split()[0])

print(f"Seu nome em maiúsculas é {nomeMaiusculo}.")
print(f"Seu nome em minúsculas é {nomeMinusculo}.")
print(f"Seu nome tem ao todo {totalLetras} letras.")
print(f"Seu primeiro nome tem {letrasPrimeiroNome} letras.")
