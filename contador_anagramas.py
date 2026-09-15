import math

### Fórmula original utilizada -> | n! / (f1! * f2!... fk!) |

def porcentagem(numero):
    res = (1 / numero) * 100

    return res

def contar_anagramas(palavra):
    letras = { }

    for letra in palavra:
        letras[letra] = letras.get(letra, 0) + 1

    produto_denominadores = 1
    for valor in letras.values():
        produto_denominadores *= math.factorial(valor)

    return math.factorial(len(palavra)) // produto_denominadores


palavra_original = input("Digite uma palavra -> ")

print(f"\nPalavra original -> {palavra_original}\n"
      f"Quantidade de Anagramas -> {contar_anagramas(palavra_original)}\n"
      f"Chance da palavra aparecer dentre os anagramas -> {porcentagem(contar_anagramas(palavra_original)):.4f}%")