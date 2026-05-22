class Pessoa:
    def __init__(self, nome, cpf, telefone, email): 
        self.__nome = nome 
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email

    @property # O jeito que se implementa o Getter
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter # O jeito que se implementa o Setter
    def telefone(self, novo_telefone):
        # Validação: só aceita se tiver pelo menos 8 caracteres
        if len(novo_telefone) >= 8:
            self.__telefone = novo_telefone
            print("Telefone atualizado com sucesso!")
        else:
            print("Erro: O número de telefone inserido é muito curto.")

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        # Validação: só aceita se tiver um '@' e um '.' no texto
        if "@" in novo_email and "." in novo_email:
            self.__email = novo_email
            print("E-mail atualizado com sucesso!")
        else:
            print("Erro: Formato de e-mail inválido.")