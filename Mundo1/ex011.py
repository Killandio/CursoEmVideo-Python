# Read the dimensions of the wall
altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))

# Calculate the area of the wall and the required amount of paint
area = altura * largura
tinta_necessaria = area / 2  # 1 liter of paint covers 2 m²

print(f"A área da parede é {area:.2f} m² e você precisará de {tinta_necessaria:.2f} litros de tinta.")
