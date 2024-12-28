# This program checks if three line segments can form a triangle by verifying if the sum of two sides
# is always greater than the third side. Additionally, it classifies the triangle as Equilateral,
# Isosceles, or Scalene if it can be formed.

lado1 = float(input("Informe o comprimento do primeiro lado: "))
lado2 = float(input("Informe o comprimento do segundo lado: "))
lado3 = float(input("Informe o comprimento do terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Sim, esses lados podem formar um triângulo!")

    if lado1 == lado2 == lado3:
        print("O triângulo formado é Equilátero (todos os lados iguais).")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo formado é Isósceles (dois lados iguais).")
    else:
        print("O triângulo formado é Escaleno (todos os lados diferentes).")
else:
    print("Esses lados NÃO conseguem formar um triângulo!")
