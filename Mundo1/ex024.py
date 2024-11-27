# This program checks if the name of a city starts with the word "Santo".

cidade = input("Digite o nome de uma cidade: ").strip()

comecaComSanto = cidade[:5].lower() == "santo"

print(f"A cidade começa com 'Santo'? {comecaComSanto}")
