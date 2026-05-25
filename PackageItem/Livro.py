from Item import Item

class Livro(Item):
    def __init__(self, id_item, esta_disponivel, titulo, ano_publicacao, autor, isbn, numero_paginas):
        super().__init__(id_item, esta_disponivel, titulo, ano_publicacao)
        self.autor = autor
        self.isbn = isbn
        self.numero_paginas = numero_paginas

    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, novo_autor):
        if isinstance(novo_autor, str): # Inserido String
            self.__autor = novo_autor
        else:
            print("Erro: O autor deve ser um texto (String).")

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, novo_isbn):
        if isinstance(novo_isbn, str): # Inserido String
            self.__isbn = novo_isbn
        else:
            print("Erro: O ISBN deve ser um texto (String).")

    @property
    def numero_paginas(self):
        return self.__numero_paginas
    
    @numero_paginas.setter
    def numero_paginas(self, numero):
        if isinstance(numero, int) and numero > 0: # Inserido int e > que 0 
            self.__numero_paginas = numero
        else:
            print("Erro: O número de páginas deve ser um número inteiro positivo.")

    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"ISBN: {self.isbn}")
        print(f"Número de Páginas: {self.numero_paginas}")
        print(f"Status: {'Disponível' if self.esta_disponivel else 'Indisponível'}")