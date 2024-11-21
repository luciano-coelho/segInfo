"""
Cifra de César.
Criptografa e descriptografa mensagens usando um deslocamento fixo no alfabeto.

"""

def cifra_cesar(texto, deslocamento, modo="criptografar"):
    resultado = ""
    for char in texto:
        if char.isalpha():  # Apenas letras são processadas
            base = 65 if char.isupper() else 97  # Letras maiúsculas e minúsculas
            if modo == "criptografar":
                resultado += chr((ord(char) - base + deslocamento) % 26 + base)
            elif modo == "descriptografar":
                resultado += chr((ord(char) - base - deslocamento) % 26 + base)
        else:
            resultado += char  
    return resultado

if __name__ == "__main__":
    mensagem = "OLAMUNDO"
    deslocamento = 3

    criptografado = cifra_cesar(mensagem, deslocamento, modo="criptografar")
    descriptografado = cifra_cesar(criptografado, deslocamento, modo="descriptografar")

    print("Mensagem Original:", mensagem)
    print("Mensagem Criptografada:", criptografado)
    print("Mensagem Descriptografada:", descriptografado)
