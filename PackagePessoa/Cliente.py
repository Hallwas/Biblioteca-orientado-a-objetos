from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, email, matricula):
        super().__init__(nome, cpf, telefone, email)
        self.matricula = matricula # Sem o "__" para forçar a passagem pelo setter, garante que o dado seja validado antes de ser salvo como privado
        self.multa_pendente = 0.0
        self.__historico_emprestimos = []

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, nova_matricula):
        if isinstance(nova_matricula, str):
            self.__matricula = nova_matricula
        else:
            print("Erro: A matrícula deve ser um texto (String).")

    @property
    def multa_pendente(self):
        return self.__multa_pendente
    
    @multa_pendente.setter
    def multa_pendente(self, valor):
        if isinstance(valor, (float, int)) and valor >= 0:
            self.__multa_pendente = float(valor)
        else:
            print("Erro: O valor da multa deve ser um número positivo.")

    @property
    def historico_emprestimos(self):
        return self.__historico_emprestimos
    
    #Funções
    def verificar_pendencias(self):
        # Retorna True se tiver multa, False se estiver tudo certo
        if self.multa_pendente > 0:
            # Usando self.nome herdado da classe Pessoa
            print(f"Atenção: O cliente {self.nome} possui uma multa pendente de R$ {self.multa_pendente:.2f}.")
            return True
        else:
            print(f"O cliente {self.nome} não possui pendências.")
            return False

    def pagar_multa(self, valor):
        if isinstance(valor, (float, int)) and valor > 0:
            if valor <= self.multa_pendente:
                self.multa_pendente -= float(valor)
                print(f"Pagamento de R$ {valor:.2f} registrado. Multa restante: R$ {self.multa_pendente:.2f}.")
            else:
                troco = valor - self.multa_pendente
                self.multa_pendente = 0.0
                print(f"Pagamento realizado. Multa totalmente quitada! Seu troco é de R$ {troco:.2f}.")
        else:
            print("Erro: O valor do pagamento deve ser maior que zero.")