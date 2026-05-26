class Item:
    def __init__(self, id_item, esta_disponivel, titulo, ano_publicacao):
        self.id_item = id_item
        self.esta_disponivel = esta_disponivel
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    @property
    def id_item(self):
        return self.__id_item
    
    @id_item.setter
    def id_item(self, novo_id):
        self.__id_item = novo_id

    @property
    def esta_disponivel(self):
        return self.__esta_disponivel
    
    @esta_disponivel.setter
    def esta_disponivel(self, status):
        if isinstance(status, bool):
            self.__esta_disponivel = status
        else:
            print("Erro: O status deve ser um valor Booleano (True ou False).")

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, novo_titulo):
        if isinstance(novo_titulo, str) and len(novo_titulo) > 0:
            self.__titulo = novo_titulo
        else:
            print("Erro: O título deve ser um texto não vazio.")

    @property
    def ano_publicacao(self):
        return self.__ano_publicacao
    
    @ano_publicacao.setter
    def ano_publicacao(self, ano):
        if isinstance(ano, int) and ano > 0:
            self.__ano_publicacao = ano
        else:
            print("Erro: O ano de publicação deve ser um número inteiro positivo.")

    # Método base de exibição — será sobrescrito (override) por Livro e Revista
    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"Status: {'Disponível' if self.esta_disponivel else 'Indisponível'}")

    def emprestar(self):
        if self.__esta_disponivel == True:
            self.__esta_disponivel = False
            print(f"Sucesso: O item '{self.titulo}' foi emprestado.")
        else:
            print(f"Atenção: O item '{self.titulo}' já está emprestado.")

    def devolver(self):
        self.__esta_disponivel = True
        print(f"O item '{self.titulo}' foi devolvido com sucesso.")
