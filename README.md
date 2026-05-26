# Sistema de Biblioteca — Programação Orientada a Objetos

Trabalho final da disciplina de Programação Orientada a Objetos.  
Implementação de um sistema de gerenciamento de biblioteca utilizando os principais conceitos de POO em **Python**.

---

## Integrantes

- André Hallwass
- João Gabriel Dal Forno Casagrande

---

## Problema a ser resolvido

Gerenciar o acervo de uma biblioteca, controlando empréstimos de livros e revistas, cadastro de clientes e aplicação automática de multas por atraso na devolução.

### Principais funcionalidades

- Cadastro de itens no acervo (livros e revistas)
- Cadastro de clientes e bibliotecários
- Controle de empréstimos com data de devolução
- Cálculo automático de multa por atraso (R$ 2,50/dia)
- Pagamento de multas com cálculo de troco
- Busca de itens no acervo
- Exibição de dados de cada tipo de item

---

## Estrutura do projeto

```
Biblioteca-orientado-a-objetos/
│
├── main.py                        # Fluxo principal de execução
│
├── Item.py                        # Classe base abstrata para itens do acervo
├── Pessoa.py                      # Classe base para pessoas
├── Biblioteca.py                  # Classe que gerencia o acervo e usuários
├── Emprestimo.py                  # Classe que representa um contrato de empréstimo
│
├── PackageItem/
│   ├── Livro.py                   # Subclasse de Item — representa um livro
│   └── Revista.py                 # Subclasse de Item — representa uma revista
│
├── PackagePessoa/
│   ├── Cliente.py                 # Subclasse de Pessoa — usuário da biblioteca
│   └── Bibliotecario.py           # Subclasse de Pessoa — funcionário
│
├── .gitignore
└── README.md
```

---

## Como executar

### Pré-requisitos

- Python 3.8 ou superior instalado

### Executar

```bash
# Clone o repositório
git clone https://github.com/Hallwas/Biblioteca-orientado-a-objetos.git
cd Biblioteca-orientado-a-objetos

# Execute o programa principal
python main.py
```

---

## Regras de negócio implementadas

### 1. Autorização de empréstimo — `Bibliotecario.autorizar_emprestimo()`
O bibliotecário verifica se o item está disponível antes de autorizar o empréstimo. Se o item já estiver emprestado, o empréstimo é negado.

### 2. Cálculo de multa por atraso — `Emprestimo.calcular_multa()`
Ao devolver um item, o sistema compara a data atual com a data de devolução prevista. Se houver atraso, aplica uma multa de **R$ 2,50 por dia de atraso**.

---

## Exemplo de saída

```
Sucesso: O item 'O Senhor dos Anéis' foi adicionado ao acervo da biblioteca.
Sucesso: O item 'Superinteressante' foi adicionado ao acervo da biblioteca.
Sucesso: Usuário 'André Hallwass' cadastrado.

Iniciando um empréstimo
Bibliotecário(a) João Casagrande autorizou o empréstimo do item 'O Senhor dos Anéis'.
Sucesso: O item 'O Senhor dos Anéis' foi emprestado.

Devolução de multas
Atraso detectado: Aplicando multa de R$ 5.00 ao cliente André Hallwass.
Atenção: O cliente André Hallwass possui uma multa pendente de R$ 5.00.
Pagamento realizado. Multa totalmente quitada! Seu troco é de R$ 5.00.
O item 'O Senhor dos Anéis' foi devolvido com sucesso.
Empréstimo finalizado com sucesso.

Testando a exibição de dados
Título: O Senhor dos Anéis
Autor: J.R.R. Tolkien
Ano de Publicação: 1954
ISBN: 978-0007136599
Número de Páginas: 1178
Status: Disponível
```
