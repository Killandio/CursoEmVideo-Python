# Function that receives multiple numbers and returns the largest one.

def main():
    maior(2, 9, 4, 5, 7, 1)
    maior(4, 7, 0)
    maior(1, 2)
    maior(6)
    maior()

def maior(*numeros):
    print(f"Os números recebidos foram: {numeros}")
    if numeros:
        print(f"O maior número é: {max(numeros)}")
    else:
        print("Nenhum número foi informado.")

main()
