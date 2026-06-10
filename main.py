from datetime import date, timedelta
 
from Biblioteca import Biblioteca
from PackageItem.Livro import Livro
from PackageItem.Revista import Revista
from PackagePessoa.Cliente import Cliente
from PackagePessoa.Bibliotecario import Bibliotecario
from Emprestimo import Emprestimo
 
# Instanciando a Biblioteca
minha_biblioteca = Biblioteca(nome="Biblioteca Python")
 
# Instanciando Itens
livro1 = Livro(id_item=1, esta_disponivel=True, titulo="O Senhor dos Anéis", ano_publicacao=1954, autor="J.R.R. Tolkien", isbn="978-0007136599", numero_paginas=1178)
revista1 = Revista(id_item=2, esta_disponivel=True, titulo="Superinteressante", ano_publicacao=2023, edicao=450, mes_publicado=10)
 
# Populando a Biblioteca
minha_biblioteca.adicionar_item(livro1)
minha_biblioteca.adicionar_item(revista1)
 
# Instanciando Pessoas
cliente_andre = Cliente(nome="André Hallwass", cpf="111.222.333-44", telefone="99998888", email="andre@email.com", matricula="204912")
bibliotecario_joao = Bibliotecario(nome="João Casagrande", cpf="555.666.777-88", telefone="77776666", email="joao@email.com", id_funcionario=101, turno_trabalho="Manhã")
 
minha_biblioteca.cadastrar_usuario(cliente_andre)
 
print("\nIniciando um empréstimo")
 
# Simulando uma data de devolução para 2 dias atrás (forçar o sistema a gerar uma multa)
data_vencida = date.today() - timedelta(days=2)
 
# Criando o recibo do empréstimo
contrato_emprestimo = Emprestimo(item=livro1, cliente=cliente_andre, data_devolucao=data_vencida, esta_ativo=True)
 
# Regra de Negócio: Bibliotecário tenta autorizar o empréstimo
autorizado = bibliotecario_joao.autorizar_emprestimo(contrato_emprestimo)
 
if autorizado:
    livro1.emprestar()
 
print("\nDevolução de multas")
 
# Regra de Negócio: Calculando multa na devolução
valor_multa = contrato_emprestimo.calcular_multa()
 
if valor_multa > 0:
    print(f"Atraso detectado: Aplicando multa de R$ {valor_multa:.2f} ao cliente {cliente_andre.nome}.")
    cliente_andre.multa_pendente = valor_multa
   
    # Cliente verifica pendências e decide pagar
    cliente_andre.verificar_pendencias()
    cliente_andre.pagar_multa(10.00) # João dá uma nota de 10 reais para pagar a multa de 5 reais
 
# Finaliza o empréstimo
contrato_emprestimo.finalizar_emprestimo()
 
print("\nTestando a exibição de dados")
livro1.exibir_dados()