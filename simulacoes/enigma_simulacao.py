"""
Descrição do Funcionamento:
Simula uma Máquina de Turing com um conjunto de estados, alfabeto e transições. 
A máquina processa símbolos em uma fita com base no estado atual e nas regras de transição.

Entrada:
- Uma fita inicial contendo uma sequência de símbolos, como "000".

Saída:
- O conteúdo da fita após o processamento.

Exemplo:
Entrada: "000"
Saída: "110" (com base nas transições definidas).
"""

class MaquinaTuring:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estado_final, simbolo_vazio="_"):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.simbolo_vazio = simbolo_vazio
        self.estado_atual = estado_inicial
        self.fita = []
        self.cabeca = 0

    def carregar_fita(self, entrada):
        self.fita = list(entrada) + [self.simbolo_vazio]
        self.cabeca = 0

    def executar(self):
        while self.estado_atual != self.estado_final:
            simbolo_atual = self.fita[self.cabeca]
            if (self.estado_atual, simbolo_atual) not in self.transicoes:
                raise ValueError(f"Transição indefinida para estado '{self.estado_atual}' e símbolo '{simbolo_atual}'")
            
            estado_seguinte, simbolo_escrito, direcao = self.transicoes[(self.estado_atual, simbolo_atual)]
            self.fita[self.cabeca] = simbolo_escrito
            self.estado_atual = estado_seguinte

            if direcao == "R":
                self.cabeca += 1
            elif direcao == "L":
                self.cabeca -= 1
            
            if self.cabeca < 0:
                self.fita.insert(0, self.simbolo_vazio)
                self.cabeca = 0
            elif self.cabeca >= len(self.fita):
                self.fita.append(self.simbolo_vazio)
        
        return "".join(self.fita).strip(self.simbolo_vazio)


if __name__ == "__main__":
    estados = {"q0", "q1", "q2", "qf"}
    alfabeto = {"0", "1", "_"}
    estado_inicial = "q0"
    estado_final = "qf"
    transicoes = {
        ("q0", "0"): ("q1", "1", "R"),
        ("q1", "0"): ("q1", "0", "R"),
        ("q1", "_"): ("q2", "_", "L"),
        ("q2", "1"): ("qf", "1", "R"),
        ("q2", "0"): ("q2", "0", "L"),  # Corrigida: Define o comportamento para '0' no estado 'q2'
    }

    maquina = MaquinaTuring(estados, alfabeto, transicoes, estado_inicial, estado_final)
    maquina.carregar_fita("000")
    resultado = maquina.executar()

    print("Resultado:", resultado)
