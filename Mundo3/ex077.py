# Program that stores words in a tuple and displays the vowels in each word.

def main():
    palavras = (
        "casa", "computador", "python", "janela", "teclado",
        "programacao", "cadeira", "livro", "mesa", "telefone"
    )

    for palavra in palavras:
        print(f"A palavra '{palavra}' tem as vogais:", end=" ")
        temVogal = False
        for letra in palavra:
            if letra in "aeiou":
                print(letra, end=" ")
                temVogal = True
        if not temVogal:
            print("Nenhuma vogal")
        else:
            print()  # Line break

main()
