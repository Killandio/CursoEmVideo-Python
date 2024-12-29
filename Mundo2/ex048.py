# Loops through numbers from 1 to 500, summing odd multiples of three

soma = 0
contador = 0
for i in range(1, 500):
    if i % 3 == 0 and i % 2 == 1:
        soma += i
        contador += 1
    else:
        pass
print(f"Um total de {contador} números foram somados entre si e resultado foi {soma}")
