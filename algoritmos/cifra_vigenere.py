"""
Cifra de Vigenère.
Criptografa e descriptografa mensagens usando uma chave repetitiva.
"""

def cifra_vigenere(texto, chave, modo="criptografar"):
    resultado = ""
    chave_repetida = (chave * ((len(texto) // len(chave)) + 1))[:len(texto)]  # Repetir chave
    for t, k in zip(texto, chave_repetida):
        if t.isalpha():
            base = 65 if t.isupper() else 97
            deslocamento = ord(k.lower()) - 97  # Calcula o deslocamento com base na chave
            if modo == "criptografar":
                resultado += chr((ord(t) - base + deslocamento) % 26 + base)
            elif modo == "descriptografar":
                resultado += chr((ord(t) - base - deslocamento) % 26 + base)
        else:
            resultado += t
    return resultado

if __name__ == "__main__":
    mensagem = "OLAMUNDO"
    chave = "CHAVE"

    criptografado = cifra_vigenere(mensagem, chave, modo="criptografar")
    descriptografado = cifra_vigenere(criptografado, chave, modo="descriptografar")

    print("Mensagem Original:", mensagem)
    print("Mensagem Criptografada:", criptografado)
    print("Mensagem Descriptografada:", descriptografado)
