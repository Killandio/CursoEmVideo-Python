# This program checks if three line segments can form a triangle by verifying if the sum of two sides
# is always greater than the third side. If any condition fails, a triangle cannot be formed.

lado1 = float(input("Informe o comprimento do primeiro lado: "))
lado2 = float(input("Informe o comprimento do segundo lado: "))
lado3 = float(input("Informe o comprimento do terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Esses lados podem formar um triângulo!")
else:
    print("Esses lados NÃO conseguem formar um triângulo!")
