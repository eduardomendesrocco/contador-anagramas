def comparar_anagramas(palavra1, palavra2):
    letras_1, letras_2 = { }, { }

    for letra in palavra1:
        letras_1[letra] = letras_1.get(letra, 0) + 1
    for letra in palavra2:
        letras_2[letra] = letras_2.get(letra, 0) + 1

    if letras_1 == letras_2:
        return f"As palavras {palavra1} e {palavra2} são anagramas uma da outra!"
    else:
        return f"As palavras não são anagramas uma da outra..."

primeira_palavra, segunda_palavra = map(str, input("Digite duas palavras separadas por espaço -> ").split())
print(f"{comparar_anagramas(primeira_palavra, segunda_palavra)}")