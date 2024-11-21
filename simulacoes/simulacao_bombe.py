"""
Simulação Simplificada da Bombe.
Reduzimos o espaço de busca para tornar a simulação mais prática e rápida.
"""

import itertools

# Função para criptografar com Enigma simplificada
def enigma_simples(texto, chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapeamento = {c: chave[i] for i, c in enumerate(alfabeto)}
    return "".join(mapeamento.get(c, c) for c in texto)

# Função para descriptografar
def enigma_reversa(texto, chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapeamento_inverso = {chave[i]: c for i, c in enumerate(alfabeto)}
    return "".join(mapeamento_inverso.get(c, c) for c in texto)

# Simulação da Bombe com espaço de busca reduzido
def bombe_simulada(ciphertext, plaintext_esperado, alfabeto_reduzido):
    for permutacao in itertools.permutations(alfabeto_reduzido):
        chave_teste = "".join(permutacao) + alfabeto[len(alfabeto_reduzido):]
        decifrado = enigma_reversa(ciphertext, chave_teste)
        if plaintext_esperado in decifrado:
            return chave_teste, decifrado
    return None, None

if __name__ == "__main__":
    # Limitar o alfabeto para reduzir o espaço de busca
    alfabeto_reduzido = "ABCDEF"
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Mensagem e chave original
    chave_original = "FBADCEGHIJKLMNOPQRSTUVWXYZ" 
    mensagem = "AULA"
    criptografado = enigma_simples(mensagem, chave_original)

    # Palavra esperada no texto decifrado
    texto_esperado = "AULA"

    # Executa a simulação da Bombe
    chave_encontrada, mensagem_decifrada = bombe_simulada(criptografado, texto_esperado, alfabeto_reduzido)

    print("Mensagem Criptografada:", criptografado)
    if chave_encontrada:
        print("Chave Encontrada:", chave_encontrada)
        print("Mensagem Decifrada:", mensagem_decifrada)
    else:
        print("Nenhuma chave válida encontrada.")
