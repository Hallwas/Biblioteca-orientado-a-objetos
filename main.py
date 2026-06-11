from datetime import date, timedelta
 
from Biblioteca import Biblioteca
from PackageItem.Livro import Livro
from PackageItem.Revista import Revista
from PackagePessoa.Cliente import Cliente
from PackagePessoa.Bibliotecario import Bibliotecario
from Emprestimo import Emprestimo
 
 
# Instanciando
minha_biblioteca = Biblioteca(nome="Biblioteca Python")
 
livro1   = Livro(id_item=1, esta_disponivel=True, titulo="O Senhor dos Anéis",ano_publicacao=1954, autor="J.R.R. Tolkien",isbn="978-0007136599", numero_paginas=1178)
 
revista1 = Revista(id_item=2, esta_disponivel=True, titulo="Superinteressante",ano_publicacao=2023, edicao=450, mes_publicado=10)
 
minha_biblioteca.adicionar_item(livro1)
minha_biblioteca.adicionar_item(revista1)
 
cliente_andre      = Cliente(nome="André Hallwass", cpf="111.222.333-44",telefone="99998888", email="andre@email.com",matricula="204912")
bibliotecario_joao = Bibliotecario(nome="João Casagrande", cpf="555.666.777-88",telefone="77776666", email="joao@email.com",id_funcionario=101, turno_trabalho="Manhã")
 
minha_biblioteca.cadastrar_usuario(cliente_andre)
 
# CENÁRIO 1 - livro
print("\nIniciando o empréstimo de um livro")

data_vencida = date.today() - timedelta(days=2)
 
# Criando o recibo do empréstimo
contrato_livro = Emprestimo(item=livro1, cliente=cliente_andre, data_devolucao=data_vencida, esta_ativo=True)
 
# Regra de Negócio 1
autorizado = bibliotecario_joao.autorizar_emprestimo(contrato_livro)
if autorizado:
    livro1.emprestar()
 
# Regra de Negócio 2
valor_multa = contrato_livro.calcular_multa()
 
if valor_multa > 0:
    print(f"Atraso detectado: Aplicando multa de R$ {valor_multa:.2f} ao cliente {cliente_andre.nome}.")
    cliente_andre.multa_pendente = valor_multa
    cliente_andre.verificar_pendencias()
    cliente_andre.pagar_multa(10.00)
 
contrato_livro.finalizar_emprestimo()

# CENÁRIO 2 — Revista
print("\nIniciando o empréstimo de uma revista")

# Busca
item_encontrado = minha_biblioteca.buscar_item("Superinteressante")
 
data_futura       = date.today() + timedelta(days=5)
contrato_revista  = Emprestimo(item=item_encontrado, cliente=cliente_andre,data_devolucao=data_futura, esta_ativo=True)
 
# Regra de Negócio 1
autorizado_revista = bibliotecario_joao.autorizar_emprestimo(contrato_revista)
if autorizado_revista:
    revista1.emprestar()
 
# Regra de Negócio 2
valor_multa_revista = contrato_revista.calcular_multa()
if valor_multa_revista > 0:
    print(f"Atraso detectado: aplicando multa de R$ {valor_multa_revista:.2f}.")
    cliente_andre.multa_pendente = valor_multa_revista
else:
    print("Devolução no prazo: nenhuma multa aplicada.")
    cliente_andre.verificar_pendencias()  # Confirma que cliente está sem pendências
 
contrato_revista.finalizar_emprestimo()
 
# EXIBIÇÃO DE DADOS — demonstra o override de exibir_dados()
print("\nTestando a exibição de dados")
print("\n-- Livro --")
livro1.exibir_dados()
print("\n-- Revista --")
revista1.exibir_dados()