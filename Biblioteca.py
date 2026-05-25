class Biblioteca():
    def __init__(self, nome):
        self.nome = nome
        # As listas começam vazias quando a biblioteca é instanciada
        self.__lista_acervo = []
        self.__lista_emprestimo = []
        self.__lista_usuarios = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def lista_acervo(self):
        return self.__lista_acervo
    
    @property
    def lista_emprestimo(self):
        return self.__lista_emprestimo
    
    @property
    def lista_usuarios(self):
        return self.__lista_usuarios
    
    #Funções
    def adicionar_item(self, novo_item):
        self.lista_acervo.append(novo_item) # Adiciona um elemento ao final da lista
        
        # Item atributo titulo
        print(f"Sucesso: O item '{novo_item.titulo}' foi adicionado ao acervo da biblioteca.") 

    def cadastrar_usuario(self, novo_usuario):
        self.lista_usuarios.append(novo_usuario)
        print(f"Sucesso: Usuário '{novo_usuario.nome}' cadastrado.")

    def buscar_item(self, titulo):
        # loop de busca
        for item in self.lista_acervo:
            # Se o título do item atual for igual ao título que estamos procurando
            if item.titulo == titulo:
                print(f"Item encontrado: '{titulo}'")
                return item # Retorna o objeto inteiro do Item
        # Se não tiver nada no acervo
        print(f"Aviso: O item '{titulo}' não foi encontrado no acervo.")
        return None