import string
import itertools


def login(username, password):
    if username == "admin" and password == "aaaaaa":
        return "Login bem-sucedido!"
    else:
        return "Falha no login."

# Função para gerar senhas dinamicamente
def generate_passwords():
    characters = string.ascii_lowercase  # Senhas compostas por letras minúsculas
    for length in range(1, 10):  # Gerar senhas de tamanho 1 até 6
        for pwd in itertools.product(characters, repeat=length):
            yield ''.join(pwd)  # Gerar cada senha como uma string


# Simulação de força bruta
password_generator = generate_passwords()

# Variáveis para contar tentativas
attempts = 0

# Loop para testar senhas até encontrar a correta
while True:
    pwd = next(password_generator)  # Gerar a próxima senha dinamicamente
    attempts += 1
    print(f"Tentativa {attempts}: Tentando login com a senha: {pwd}")

    result = login("admin", pwd)  # Tentativa de login com o username "admin"

    if result == "Login bem-sucedido!":
        print(f"Senha correta encontrada após {attempts} tentativas: {pwd}")
        break  # Encerra o loop quando a senha correta for encontrada
    else:
        print(f"Resultado: {result}")
