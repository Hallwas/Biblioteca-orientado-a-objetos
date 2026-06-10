class Pessoa:
    def __init__(self, nome, cpf, telefone, email): 
        self.__nome = nome #__ -> implementa o "private do python", possui por não possuir setter
        self.__cpf = cpf
        self.telefone = telefone
        self.email = email

    @property # Getter
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter # Setter
    def telefone(self, novo_telefone):
        if len(novo_telefone) >= 8:
            self.__telefone = novo_telefone
        else:
            print("Erro: O número de telefone inserido é muito curto.")

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        if "@" in novo_email and "." in novo_email:
            self.__email = novo_email
        else:
            print("Erro: Formato de e-mail inválido.")

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")