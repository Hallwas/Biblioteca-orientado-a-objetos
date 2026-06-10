from Pessoa import Pessoa

class Bibliotecario(Pessoa): #Herda de Pessoa
    def __init__(self, nome, cpf, telefone, email, id_funcionario, turno_trabalho):
        super().__init__(nome, cpf, telefone, email) # Chama o contrutor da classe mãe para inicializar os dados
        self.id_funcionario = id_funcionario
        self.turno_trabalho = turno_trabalho

    @property
    def id_funcionario(self):
        return self.__id_funcionario
    
    @id_funcionario.setter
    def id_funcionario(self, novo_id):
        if isinstance(novo_id, int):
            self.__id_funcionario = novo_id
        else:
            print("Erro: O ID do funcionário deve ser um número inteiro.")

    @property
    def turno_trabalho(self):
        return self.__turno_trabalho
    
    @turno_trabalho.setter
    def turno_trabalho(self, novo_turno):
        self.__turno_trabalho = novo_turno

    #Funções
    def autorizar_emprestimo(self, emprestimo): #
        if emprestimo.item.esta_disponivel == True:
            # self.nome herdado de Pessoa
            print(f"Bibliotecário(a) {self.nome} autorizou o empréstimo do item '{emprestimo.item.titulo}'.")
            return True
        else:
            print(f"Empréstimo negado por {self.nome}: O item já está emprestado ou indisponível.")
            return False