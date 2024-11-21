"""
Cifra de Hill.
Criptografa e descriptografa mensagens usando álgebra linear com matrizes.
Instale o NumPy: pip install numpy
"""

import numpy as np

def cifra_hill(texto, matriz, modo="criptografar"):
    texto = texto.upper().replace(" ", "")
    tamanho = len(matriz)
    while len(texto) % tamanho != 0:
        texto += "X"  # Preenche com 'X' se necessário

    matriz = np.array(matriz)
    if modo == "descriptografar":
        determinante = int(round(np.linalg.det(matriz)))
        inverso = pow(determinante, -1, 26)  # Inverso modular
        matriz = (inverso * np.round(np.linalg.inv(matriz) * determinante).astype(int)) % 26

    resultado = ""
    for i in range(0, len(texto), tamanho):
        bloco = [ord(char) - 65 for char in texto[i:i + tamanho]]
        criptografado = np.dot(matriz, bloco) % 26
        resultado += "".join(chr(int(num) + 65) for num in criptografado)

    return resultado


if __name__ == "__main__":
    mensagem = "HELPME"
    matriz_chave = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]  # Matriz 3x3

    criptografado = cifra_hill(mensagem, matriz_chave, modo="criptografar")
    descriptografado = cifra_hill(criptografado, matriz_chave, modo="descriptografar")

    print("Mensagem Original:", mensagem)
    print("Mensagem Criptografada:", criptografado)
    print("Mensagem Descriptografada:", descriptografado)
