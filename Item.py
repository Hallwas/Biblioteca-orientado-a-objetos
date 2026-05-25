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
        # Só recebe True ou False
        if isinstance(status, bool):
            self.__esta_disponivel = status
        else:
            print("Erro: O status deve ser um valor Booleano (True ou False).")

    #Funções
    def emprestar(self):
        # Verifica o atributo privado para saber se pode emprestar
        if self.__esta_disponivel == True:
            self.__esta_disponivel = False
            print(f"Sucesso: O item '{self.titulo}' foi emprestado.")
        else:
            print(f"Atenção: O item '{self.titulo}' já está emprestado.")

    def devolver(self):
        self.__esta_disponivel = True
        print(f"O item '{self.titulo}' foi devolvido com sucesso.")