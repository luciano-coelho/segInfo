"""
Cifra de Substituição Simples.
Criptografa e descriptografa mensagens usando uma substituição alfabética fixa.
"""

def gerar_chave_substituicao():
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    substituicao = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    return {c: substituicao[i] for i, c in enumerate(alfabeto)}


def cifra_substituicao(texto, chave, modo="criptografar"):
    texto = texto.upper().replace(" ", "")
    inversa = {v: k for k, v in chave.items()}
    resultado = ""
    for char in texto:
        if modo == "criptografar":
            resultado += chave.get(char, char)
        else:
            resultado += inversa.get(char, char)
    return resultado


if __name__ == "__main__":
    mensagem = "HELLO SIMPLE"
    chave = gerar_chave_substituicao()

    criptografado = cifra_substituicao(mensagem, chave, modo="criptografar")
    descriptografado = cifra_substituicao(criptografado, chave, modo="descriptografar")

    print("Mensagem Original:", mensagem)
    print("Mensagem Criptografada:", criptografado)
    print("Mensagem Descriptografada:", descriptografado)
