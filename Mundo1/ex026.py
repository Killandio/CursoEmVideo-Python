# This program reads a sentence and displays:
# 1. How many times the letter "A" appears.
# 2. The position of the first occurrence of "A".
# 3. The position of the last occurrence of "A".

frase = input("Digite uma frase: ").strip().lower()

quantidadeDeA = frase.count("a")
primeiraPosicao = frase.find("a") + 1
ultimaPosicao = frase.rfind("a") + 1

print(f"A letra 'A' aparece {quantidadeDeA} vezes.")
print(f"A primeira letra 'A' aparece na posição {primeiraPosicao}.")
print(f"A última letra 'A' aparece na posição {ultimaPosicao}.")
