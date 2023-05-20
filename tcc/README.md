# TCC-II
Plataforma Web para Gerenciamento de Riscos





## A aplicação:
# **Configurações iniciais:**

Criar um ambiente virtual

```python
# Criar
	# Linux
		python3 -m venv venv
	# Windows
		python -m venv venv
```

Após a criação do ambiente (venv). Ativa-lo:

```python
# Ativar
	# Linux
		source venv/bin/activate
	# Windows
		venv\Scripts\Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Fazer a instalação das dependências do projeto:

```python
pip install -r requirements.txt
```



## Atores

### Administrador
- Cadastrar um empregado
- Cadastrar uma empresa
- Cadastrar um inventário de riscos
- Cadastrar um plano de ação

- Editar um empregado
- Editar uma empresa
- Editar um inventário de riscos
- Editar um plano de ação

- Deletar um empregado
- Deletar uma empresa
- Deletar um inventário de riscos
- Deletar um plano de ação

### Empregados
- Visualizar a sua empresa
- Visualizar o seu inventário de riscos
- Visualizar o seu plano de ação

## Tabelas

### Empresa
### Empregado 
### Inventário
### Avaliacao
### Plano de ação



## Levantamento de Requisitos de Software

### Requisitos Funcionais
## Levantamento de Requisitos de Software

## Requisitos Funcionais

- Todos os empregados devem possuir um cadastro com usuário e senha.
- Todos os empregados logados no sistema podem visualizar o seu inventário de riscos.
- Todos os empregados logados no sistema podem visualizar o seu plano de ação.

### Requisitos Não-Funcionais
## Requisitos Não-Funcionais

- O sistema deve ser acessado com usuário e senha.
- O sistema deve mostrar uma tabela contendo o inventário de riscos dos usuários.
- O sistema deve mostrar uma tabela contendo o plano de ação dos usuários.
- O sistema não permite alteração do plano de ação pelos usuários.
- O preenchimento dos campos da empresa são obrigatórios.
- O preenchimento dos campos do inventário de riscos são obrigatórios.
- O preenchimento dos campos do plano de ação são obrigatórios.

### Front-End
## *sistema de login e senha*
- O acesso será validado pelo metodo Authenticate do django, e será realizado digitando o nome do usuário e a senha.

## Front-End
- [x] Django
- [x] Html
- [x] Css
- [x] Javascript
- [x] Bootstrap 4

### Back-End
## Back-End
- [x] Python
- [x] Django

## Criar os diagramas utilizando o graph_models:
python manage.py graph_models -a -o pgr_models.png


### Algumas ScreenShots
## Card de Cadastro
## Card de Login
## Card de Home
## Card da Usuario
## Card da Empresa
## Card de Inventario
## Card do Plano de Ação
