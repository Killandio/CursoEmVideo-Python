# Program that stores the top 20 teams of the Brazilian Championship in a tuple.
# The user can choose different options to view the rankings.

def main():
    timesBrasileirao = (
        "Palmeiras", "Internacional", "Fluminense", "Corinthians", "Flamengo",
        "Athletico-PR", "Atlético-MG", "Fortaleza", "São Paulo", "América-MG",
        "Botafogo", "Santos", "Goiás", "Bragantino", "Coritiba",
        "Cuiabá", "Ceará", "Atlético-GO", "Avaí", "Chapecoense"
    )

    while True:
        print("\n--- Menu Brasileirão ---")
        print("1 - Mostrar os 5 primeiros colocados")
        print("2 - Mostrar os últimos 4 colocados")
        print("3 - Mostrar times em ordem alfabética")
        print("4 - Mostrar posição da Chapecoense")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nOs 5 primeiros colocados são:")
            for i in range(5):
                print(f"{i + 1}° - {timesBrasileirao[i]}")

        elif opcao == "2":
            print("\nOs últimos 4 colocados são:")
            for i in range(-4, 0):
                print(f"{len(timesBrasileirao) + i + 1}° - {timesBrasileirao[i]}")

        elif opcao == "3":
            print("\nTimes em ordem alfabética:")
            for time in sorted(timesBrasileirao):
                print(time)

        elif opcao == "4":
            print("\nPosição da Chapecoense na tabela:")
            if "Chapecoense" in timesBrasileirao:
                print(f"Chapecoense está na {timesBrasileirao.index('Chapecoense') + 1}ª posição.")
            else:
                print("Chapecoense não está na lista.")

        elif opcao == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Escolha um número entre 1 e 5.")


main()
