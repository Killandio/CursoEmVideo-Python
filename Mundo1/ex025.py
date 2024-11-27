# This program checks if the name entered by the user contains the word "Silva".

nome = input("Digite seu nome completo: ").strip()

temSilva = "silva" in nome.lower()

print(f"Seu nome tem 'Silva'? {temSilva}")
