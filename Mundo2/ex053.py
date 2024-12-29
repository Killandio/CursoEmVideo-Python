# Verifies if a given phrase is a palindrome by ignoring spaces, case, and accents

def ePalindromo(frase):
    normalizada = ''.join(caractere for caractere in frase if caractere.isalnum()).lower()
    return normalizada == normalizada[::-1]

frase = input("Digite uma frase para verificar se é um palíndromo: ")

if ePalindromo(frase):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
