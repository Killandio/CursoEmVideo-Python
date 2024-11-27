# Read a value from the user (input)
valor = input("Digite algo: ")

# Display the type of the input value
tipo = type(valor)

# Check various characteristics of the input
is_numeric = valor.isnumeric()
is_alpha = valor.isalpha()
is_alnum = valor.isalnum()
is_upper = valor.isupper()
is_lower = valor.islower()
is_title = valor.istitle()

# Display the results
print(f"O tipo primitivo desse valor é {tipo}")
print(f"É um número? {is_numeric}")
print(f"É alfabético? {is_alpha}")
print(f"É alfanumérico? {is_alnum}")
print(f"Está em maiúsculas? {is_upper}")
print(f"Está em minúsculas? {is_lower}")
print(f"Está capitalizado? {is_title}")
