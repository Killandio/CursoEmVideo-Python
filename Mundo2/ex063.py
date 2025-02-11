# Generates a sequence of Fibonacci numbers up to the
# specified term

from sympy import fibonacci

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Apenas números inteiros são permitidos")

def sequenciaFibonacci(numero):
    return [fibonacci(i) for i in range(1, numero + 1)]

numero = getInt("Digite um número para saber seus termo sda sequência de Fibonacci: ")
print(f"Os {numero} primeiros termos da sequência de Fibonacci são: {sequenciaFibonacci(numero)}")