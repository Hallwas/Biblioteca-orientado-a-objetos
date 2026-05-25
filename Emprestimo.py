from datetime import date #Bliblioteca para a manipulação de datas

class Emprestimo():
    def __init__(self, item, cliente, data_devolucao, esta_ativo):
        self.__item = item
        self.__cliente = cliente
        self.data_devolucao = data_devolucao
        self.esta_ativo = esta_ativo

    @property
    def item(self):
        return self.__item

    @property
    def cliente(self):
        return self.__cliente

    @property
    def data_devolucao(self):
        return self.__data_devolucao
    
    @data_devolucao.setter
    def data_devolucao(self, nova_data):
        # Garante que o valor passado é realmente do tipo 'date'
        if isinstance(nova_data, date):
            self.__data_devolucao = nova_data
        else:
            print("Erro: A data deve ser um objeto do tipo 'date'.")

    @property
    def esta_ativo(self):
        return self.__esta_ativo
    
    @esta_ativo.setter
    def esta_ativo(self, status):
        if isinstance(status, bool):
            self.__esta_ativo = status
        else:
            print("Erro: O status deve ser True ou False.")

    #Funções     
    def finalizar_emprestimo(self):
        # Quando o empréstimo acaba, ele deixa de estar ativo
        if self.esta_ativo:
            self.esta_ativo = False
            self.item.devolver() # Devolve o item
            print("Empréstimo finalizado com sucesso.")
        else:
            print("Atenção: Este empréstimo já estava finalizado.")

    def calcular_multa(self):
        data_hoje = date.today() # Se usa uma variavel, o programa não precisa verificar o horario duas vezes 
        
        if data_hoje > self.data_devolucao:
            dias_atraso = (data_hoje - self.data_devolucao).days
            multa = dias_atraso * 2.50  # R$ 2,50 por dia de atraso
            return float(multa)
        else:
            return 0.0  # Sem atraso, multa zero