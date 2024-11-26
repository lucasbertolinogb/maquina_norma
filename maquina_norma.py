class MaquinaNorma:
    def __init__(self):
        # Inicializa os registradores de A até H com valor 0
        self.registradores = {chr(65 + i): 0 for i in range(8)}
        self.instrucoes = {}  # Dicionário para armazenar as instruções
        self.linha_atual = 1  # Começa na instrução 1

    def inicializar_registradores(self):
        """Permite ao usuário inicializar os registradores."""
        print("Inicialize os registradores (de A a H). Deixe em branco para manter 0.")
        for reg in self.registradores:
            valor = input(f"Valor para {reg}: ")
            if valor.isdigit():
                self.registradores[reg] = int(valor)

    def carregar_instrucoes(self, arquivo):
        """Carrega as instruções do arquivo de entrada."""
        with open(arquivo, 'r') as f:
            for linha in f:
                rotulo, comando = linha.strip().split(":")
                rotulo = int(rotulo.strip())
                partes = comando.split()
                operacao = partes[0]  # Operação
                registrador = partes[1]  # Registrador
                destino1 = int(partes[2])  # Destino 1
                destino2 = int(partes[3]) if len(partes) > 3 else None
                self.instrucoes[rotulo] = (operacao, registrador, destino1, destino2)

    def executar(self):
        """Executa as instruções carregadas."""
        while self.linha_atual in self.instrucoes:
            operacao, registrador, destino1, destino2 = self.instrucoes[self.linha_atual]
            print(f"Executando linha {self.linha_atual}: {operacao} {registrador} {destino1}{',' + str(destino2) if destino2 else ''}")
            print(f"Estado antes: {self.registradores}")

            if operacao == "ADD":
                self.registradores[registrador] += 1
                self.linha_atual = destino1
            elif operacao == "SUB":
                if self.registradores[registrador] > 0:
                    self.registradores[registrador] -= 1
                self.linha_atual = destino1
            elif operacao == "ZER":
                self.linha_atual = destino1 if self.registradores[registrador] == 0 else destino2

            print(f"Estado depois: {self.registradores}")

    def multiplicacao(self, reg_a, reg_b, reg_c, reg_d):
        """Multiplica o valor de A por B usando C e D."""
        self.registradores[reg_c] = 0  # Resultado
        while self.registradores[reg_b] > 0:
            self.registradores[reg_b] -= 1
            self.registradores[reg_d] = self.registradores[reg_a]
            while self.registradores[reg_d] > 0:
                self.registradores[reg_d] -= 1
                self.registradores[reg_c] += 1

    def fatorial(self, reg_a, reg_b, reg_c, reg_d):
        """Calcula o fatorial de A usando B, C e D."""
        self.registradores[reg_c] = 1  # Resultado
        while self.registradores[reg_a] > 0:
            self.registradores[reg_b] = self.registradores[reg_a]
            self.registradores[reg_a] -= 1
            self.multiplicacao(reg_b, reg_c, reg_c, reg_d)


# Exemplo de uso:
# 1. Inicialize os registradores.
# 2. Execute as instruções carregadas.

maquina = MaquinaNorma()
maquina.inicializar_registradores()
maquina.carregar_instrucoes('instrucoes.txt')  # Substitua pelo caminho do arquivo
maquina.executar()


