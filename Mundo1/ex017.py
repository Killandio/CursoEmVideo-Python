# This program calculates the hypotenuse of a right triangle using the Pythagorean theorem
# without importing external modules.

catetoOposto = float(input("Digite o comprimento do cateto oposto: "))
catetoAdjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** 0.5

print(f"A hipotenusa do triângulo é {hipotenusa:.2f}.")
