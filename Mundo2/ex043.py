# Calculates the Body Mass Index (BMI) based on user input for weight and height.
# Classifies the BMI according to the WHO standards.

def getPosFloat(prompt):

    while True:
        try:
            numero = float(input(prompt))
            if numero > 0:
                return numero
            else:
                print("Apenas números acima de zero são válidos.")
        except ValueError:
            print("Escolha um número positivo válido para prosseguir!")

def calculaImc(peso, altura):

    return peso / (altura ** 2)

def classificaImc(imc):

    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

peso = getPosFloat("Digite o seu peso em kg: ")
altura = getPosFloat("Digite a sua altura em metros: ")

imc = calculaImc(peso, altura)

print(f"Seu IMC é {imc:.2f}.")
print(f"Classificação: {classificaImc(imc)}")
