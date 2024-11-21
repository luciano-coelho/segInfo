"""
Cifra de Playfair.
Criptografa e descriptografa mensagens usando uma matriz 5x5 gerada a partir de uma palavra-chave.
"""

def gerar_matriz_playfair(chave):
    chave = chave.upper().replace("J", "I")  # Normaliza a chave
    matriz = []
    letras_usadas = set()

    for char in chave:
        if char not in letras_usadas and char.isalpha():
            matriz.append(char)
            letras_usadas.add(char)

    for letra in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if letra not in letras_usadas:
            matriz.append(letra)
            letras_usadas.add(letra)

    return [matriz[i:i + 5] for i in range(0, 25, 5)]


def encontrar_posicao(matriz, char):
    for i, linha in enumerate(matriz):
        if char in linha:
            return i, linha.index(char)
    return None


def processar_digrama(matriz, digrama, modo):
    linha1, col1 = encontrar_posicao(matriz, digrama[0])
    linha2, col2 = encontrar_posicao(matriz, digrama[1])

    if linha1 == linha2:  # Mesma linha
        col1 = (col1 + 1) % 5 if modo == "criptografar" else (col1 - 1) % 5
        col2 = (col2 + 1) % 5 if modo == "criptografar" else (col2 - 1) % 5
    elif col1 == col2:  # Mesma coluna
        linha1 = (linha1 + 1) % 5 if modo == "criptografar" else (linha1 - 1) % 5
        linha2 = (linha2 + 1) % 5 if modo == "criptografar" else (linha2 - 1) % 5
    else:  # Retângulo
        col1, col2 = col2, col1

    return matriz[linha1][col1] + matriz[linha2][col2]


def cifra_playfair(texto, chave, modo="criptografar"):
    matriz = gerar_matriz_playfair(chave)
    texto = texto.upper().replace("J", "I").replace(" ", "")
    resultado = ""

    # Divide o texto em digramas
    digramas = []
    i = 0
    while i < len(texto):
        if i + 1 < len(texto) and texto[i] != texto[i + 1]:
            digramas.append(texto[i:i + 2])
            i += 2
        else:
            digramas.append(texto[i] + "X")
            i += 1

    for digrama in digramas:
        resultado += processar_digrama(matriz, digrama, modo)

    return resultado


if __name__ == "__main__":
    mensagem = "HELLO PLAYFAIR"
    chave = "MONARCHY"

    criptografado = cifra_playfair(mensagem, chave, modo="criptografar")
    descriptografado = cifra_playfair(criptografado, chave, modo="descriptografar")

    print("Mensagem Original:", mensagem)
    print("Mensagem Criptografada:", criptografado)
    print("Mensagem Descriptografada:", descriptografado)
