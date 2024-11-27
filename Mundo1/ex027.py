# This program reads a full name and displays:
# 1. The first name.
# 2. The last name.

nome_completo = input("Digite seu nome completo: ").strip()

primeiro_nome = nome_completo.split()[0]
ultimo_nome = nome_completo.split()[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
