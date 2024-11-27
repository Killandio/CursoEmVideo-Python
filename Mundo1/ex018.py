# This program reads an angle in degrees and calculates its sine, cosine, and tangent values.

from math import *

angulo = float(input("Digite o valor do ângulo em graus: "))

angulo_rad = radians(angulo)
seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)

print(f"O seno de {angulo}° é {seno:.2f}.")
print(f"O cosseno de {angulo}° é {cosseno:.2f}.")
print(f"A tangente de {angulo}° é {tangente:.2f}.")
