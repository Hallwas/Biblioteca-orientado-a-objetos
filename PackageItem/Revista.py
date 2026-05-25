from Item import Item

class Revista(Item):
    def __init__(self, id_item, esta_disponivel, titulo, ano_publicacao, edicao, mes_publicado):
        super().__init__(id_item, esta_disponivel, titulo, ano_publicacao)
        self.edicao = edicao
        self.mes_publicado = mes_publicado

    @property
    def edicao(self):
        return self.__edicao
    
    @edicao.setter
    def edicao(self, nova_edicao):
        if isinstance(nova_edicao, int) and nova_edicao > 0: # Inserido int e > que 0 
            self.__edicao = nova_edicao
        else:
            print("Erro: A edição deve ser um número inteiro positivo.")

    @property
    def mes_publicado(self):
        return self.__mes_publicado
    
    @mes_publicado.setter
    def mes_publicado(self, mes):
        # Tem que estar entre 1 e 12
        if isinstance(mes, int) and 1 <= mes <= 12:
            self.__mes_publicado = mes
        else:
            print("Erro: O mês de publicação deve ser um número inteiro válido (entre 1 e 12).")

    def exibir_dados(self):
        print(f"Título da Revista: {self.titulo}")
        print(f"Edição: {self.edicao}")
        print(f"Mês/Ano de Publicação: {self.mes_publicado}/{self.ano_publicacao}")
        print(f"Status: {'Disponível' if self.esta_disponivel else 'Indisponível'}")