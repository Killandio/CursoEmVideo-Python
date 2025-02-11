# Reads and validates the gender input, accepting only 'M' or 'F'

def getGender(prompt):
    while True:
        gender = input(prompt).strip().upper()
        if gender in ["M", "F"]:
            print(f"Gênero {gender} registrado com sucesso.")
            return gender
        else:
            print("Entrada inválida. Digite 'M' para masculino ou 'F' para feminino.")

getGender("Digite 'M' para masculino e 'F' para feminino: ")
