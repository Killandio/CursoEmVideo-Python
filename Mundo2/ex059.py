# Simple Calculator Program with Editable Values

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Apenas números inteiros são permitidos")

primeiroValor = [getInt("Digite um número: ")]
segundoValor = [getInt("Digite um segundo número: ")]

soma = primeiroValor[0] + segundoValor[0]
multiplicacao = primeiroValor[0] * segundoValor[0]
divisao = None
if segundoValor[0] != 0:
    divisao = primeiroValor[0] / segundoValor[0]
subtracao = primeiroValor[0] - segundoValor[0]

escolhaMenu = 0
while escolhaMenu != 7:
    print(f"\nQue operação você deseja realizar entre esses dois valores?"
          f"\n"
          f"1) Soma\n"
          f"2) Subtração\n"
          f"3) Multiplicação\n"
          f"4) Divisão\n"
          f"5) Maior Número\n"
          f"6) Editar\n"
          f"7) Sair")
    escolhaMenu = getInt("Digite o número correspondente a opção desejada: ")
    if escolhaMenu == 1:
        print(f"A soma entre {primeiroValor[0]} e {segundoValor[0]} é igual a {soma}")
    elif escolhaMenu == 2:
        print(f"A subtração de {primeiroValor[0]} por {segundoValor[0]} é igual a {subtracao}")
    elif escolhaMenu == 3:
        print(f"A multiplicação entre {primeiroValor[0]} e {segundoValor[0]} é igual a {multiplicacao}")
    elif escolhaMenu == 4:
        if segundoValor[0] == 0:
            print("Divisão por zero não é permitida.")
        else:
            divisao = primeiroValor[0] / segundoValor[0]
            print(f"A divisão de {primeiroValor[0]} por {segundoValor[0]} é igual a {divisao}")
    elif escolhaMenu == 5:
        if primeiroValor[0] > segundoValor[0]:
            print(f"{primeiroValor[0]} é maior que {segundoValor[0]}")
        elif segundoValor[0] > primeiroValor[0]:
            print(f"{segundoValor[0]} é maior que {primeiroValor[0]}")
        else:
            print("Ambos os valores são iguais")
    elif escolhaMenu == 6:
        print(f"1) O primeiro número\n"
              f"2) O segundo número\n"
              f"3) Sair\n")
        alterar = getInt("Qual número você deseja alterar?\n")
        if alterar == 1:
            novoValor = getInt("Qual novo valor você deseja adicionar no lugar do anterior?\n")
            primeiroValor[0] = novoValor
            print("Alteração executada com sucesso\n")
        elif alterar == 2:
            novoValor2 = getInt("Qual novo valor você deseja adicionar no lugar do anterior?\n")
            if novoValor2 == 0:
                print("Valor inválido: divisor não pode ser zero.\n")
            else:
                segundoValor[0] = novoValor2
                print("Alteração executada com sucesso\n")
        elif alterar == 3:
            print("Saída executada com Sucesso")
        else:
            print("Opção inválida")

        soma = primeiroValor[0] + segundoValor[0]
        multiplicacao = primeiroValor[0] * segundoValor[0]
        subtracao = primeiroValor[0] - segundoValor[0]
        if segundoValor[0] != 0:
            divisao = primeiroValor[0] / segundoValor[0]
        else:
            divisao = None
    elif escolhaMenu >= 8 or escolhaMenu <= 0:
        print("Opção inválida")
    else:
        print("Saída executada com sucesso")
